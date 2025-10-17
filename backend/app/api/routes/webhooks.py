from app.schemas.vapi import VAPIWebhookEvent, VAPIFunctionLoadedStatus, VAPIFunctionNotLoadedStatus
from app.services.webhook_service import process_vapi_webhook

router = APIRouter()


@router.post("/vapi")
async def vapi_webhook(
    webhook_data: dict,
    db: AsyncSession = Depends(get_db)
):
    """Receive and process VAPI webhooks"""
    try:
        event_type = webhook_data.get("type")
        
        if event_type == "function-call":
            await handle_function_call(webhook_data, db)
        elif event_type == "call-ended":
            await handle_call_ended(webhook_data, db)
        elif event_type == "transcript":
            await handle_transcript(webhook_data, db)
        
        return {"status": "received", "event_type": event_type}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Webhook processing error: {str(e)}"
        )


async def handle_function_call(webhook_data: dict, db: AsyncSession):
    """Handle VAPI function calls"""
    function_call = webhook_data.get("functionCall", {})
    function_name = function_call.get("name")
    parameters = function_call.get("parameters", {})
    call_id = webhook_data.get("call", {}).get("id")
    
    # Get call log
    result = await db.execute(
        select(CallLog).where(CallLog.call_sid == call_id)
    )
    call_log = result.scalar_one_or_none()
    
    if function_name == "record_loaded_status":
        # Create loaded status update
        status_update = StatusUpdate(
            call_log_id=call_log.call_id if call_log else None,
            driver_id=parameters.get("driver_id"),
            is_loaded=True,
            status_type="LOADED",
            cargo_loaded_time=parameters.get("load_completed_time"),
            departure_time=parameters.get("departure_time"),
            driver_location=parameters.get("current_location"),
            additional_notes=parameters.get("issues_notes"),
            reported_at=datetime.utcnow()
        )
        db.add(status_update)
        
        # Update load if load_id is provided
        if parameters.get("load_id"):
            load_result = await db.execute(
                select(Load).where(Load.load_id == parameters.get("load_id"))
            )
            load = load_result.scalar_one_or_none()
            if load:
                load.load_status = "LOADED"
                load.cargo_type = parameters.get("cargo_type")
                load.weight_lbs = parameters.get("weight_lbs")
                load.destination = parameters.get("destination")
                load.load_completed_time = parameters.get("load_completed_time")
        
    elif function_name == "record_not_loaded_status":
        # Create not loaded status update
        status_update = StatusUpdate(
            call_log_id=call_log.call_id if call_log else None,
            driver_id=parameters.get("driver_id"),
            is_loaded=False,
            status_type="NOT_LOADED",
            delay_reason_category=parameters.get("delay_reason_category"),
            delay_reason_details=parameters.get("delay_reason_details"),
            estimated_load_time=parameters.get("estimated_load_time"),
            waiting_duration_minutes=parameters.get("waiting_duration_minutes"),
            trucks_in_queue=parameters.get("trucks_in_queue"),
            is_recurring_issue=parameters.get("is_recurring_issue", False),
            driver_location=parameters.get("current_location"),
            reported_at=datetime.utcnow()
        )
        db.add(status_update)
    
    await db.commit()


async def handle_call_ended(webhook_data: dict, db: AsyncSession):
    """Handle call ended event"""
    call_data = webhook_data.get("call", {})
    call_id = call_data.get("id")
    
    result = await db.execute(
        select(CallLog).where(CallLog.call_sid == call_id)
    )
    call_log = result.scalar_one_or_none()
    