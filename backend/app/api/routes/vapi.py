import httpx
from app.config import get_settings
from app.schemas.vapi import VAPICallRequest, VAPICallResponse

router = APIRouter()
settings = get_settings()


@router.post("/initiate-call", response_model=VAPICallResponse)
async def initiate_vapi_call(
    call_request: VAPICallRequest,
    db: AsyncSession = Depends(get_db)
):
    """Initiate an outbound call via VAPI"""
    # Get driver details
    result = await db.execute(
        select(Driver).where(Driver.driver_id == call_request.driver_id)
    )
    driver = result.scalar_one_or_none()
    
    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with ID {call_request.driver_id} not found"
        )
    
    # Create call log entry
    call_log = CallLog(
        driver_id=call_request.driver_id,
        phone_number=call_request.phone_number,
        call_direction="OUTBOUND",
        call_status="INITIATED",
        call_initiated_at=datetime.utcnow(),
        vapi_assistant_id=settings.VAPI_ASSISTANT_ID
    )
    db.add(call_log)
    await db.commit()
    await db.refresh(call_log)
    
    # Make VAPI API call
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {settings.VAPI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "assistant": {
                "assistantId": settings.VAPI_ASSISTANT_ID
            },
            "phoneNumberId": settings.VAPI_PHONE_NUMBER_ID,
            "customer": {
                "number": call_request.phone_number,
                "name": call_request.driver_name
            }
        }
        
        try:
            response = await client.post(
                f"{settings.VAPI_BASE_URL}/call/phone",
                headers=headers,
                json=payload,
                timeout=10.0
            )
            response.raise_for_status()
            vapi_data = response.json()
            
            # Update call log with VAPI call ID
            call_log.call_sid = vapi_data.get("id")
            call_log.call_status = "RINGING"
            await db.commit()
            
            return VAPICallResponse(
                call_id=vapi_data.get("id"),
                status="initiated",
                message=f"Call initiated to {call_request.driver_name}"
            )
            
        except httpx.HTTPError as e:
            call_log.call_status = "FAILED"
            call_log.error_message = str(e)
            await db.commit()
            
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to initiate call: {str(e)}"
            )


@router.post("/bulk-call")
async def initiate_bulk_calls(
    driver_ids: List[int],
    db: AsyncSession = Depends(get_db)
):
    """Initiate calls to multiple drivers"""
    results = []
    
    for driver_id in driver_ids:
        result = await db.execute(
            select(Driver).where(Driver.driver_id == driver_id)
        )
        driver = result.scalar_one_or_none()
        
        if driver:
            try:
                call_request = VAPICallRequest(
                    driver_id=driver_id,
                    phone_number=driver.phone_number,
                    driver_name=driver.driver_name
                )
                response = await initiate_vapi_call(call_request, db)
                results.append({
                    "driver_id": driver_id,
                    "status": "success",
                    "call_id": response.call_id
                })
            except Exception as e:
                results.append({
                    "driver_id": driver_id,
                    "status": "failed",
                    "error": str(e)
                })
        else:
            results.append({
                "driver_id": driver_id,
                "status": "failed",
                "error": "Driver not found"
            })
    
    return {
        "total_drivers": len(driver_ids),
        "results": results
    }
