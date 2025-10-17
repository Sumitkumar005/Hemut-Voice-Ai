from app.models.call_log import CallLog
from app.schemas.call_log import CallLogCreate, CallLogUpdate, CallLogResponse

router = APIRouter()


@router.get("/", response_model=List[CallLogResponse])
async def get_call_logs(
    driver_id: Optional[int] = None,
    call_status: Optional[str] = Query(None, alias="status"),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all call logs with optional filters"""
    query = select(CallLog)
    
    if driver_id:
        query = query.where(CallLog.driver_id == driver_id)
    if call_status:
        query = query.where(CallLog.call_status == call_status)
    
    query = query.order_by(CallLog.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    call_logs = result.scalars().all()
    
    return call_logs


@router.get("/{call_id}", response_model=CallLogResponse)
async def get_call_log(
    call_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific call log by ID"""
    result = await db.execute(
        select(CallLog).where(CallLog.call_id == call_id)
    )
    call_log = result.scalar_one_or_none()
    
    if not call_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Call log with ID {call_id} not found"
        )
    
    return call_log


@router.get("/{call_id}/transcript")
async def get_call_transcript(
    call_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get call transcript"""
    result = await db.execute(
        select(CallLog).where(CallLog.call_id == call_id)
    )
    call_log = result.scalar_one_or_none()
    
    if not call_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Call log with ID {call_id} not found"
        )
    
    return {
        "call_id": call_id,
        "transcript": call_log.call_transcript,
        "summary": call_log.call_summary
    }


@router.post("/", response_model=CallLogResponse, status_code=status.HTTP_201_CREATED)
async def create_call_log(
    call_log: CallLogCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new call log entry"""
    db_call_log = CallLog(**call_log.model_dump())
    db.add(db_call_log)
    await db.commit()
    await db.refresh(db_call_log)
    
    return db_call_log


@router.put("/{call_id}", response_model=CallLogResponse)
async def update_call_log(
    call_id: int,
    call_log_update: CallLogUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update call log"""
    result = await db.execute(
        select(CallLog).where(CallLog.call_id == call_id)
    )
    call_log = result.scalar_one_or_none()
    
    if not call_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Call log with ID {call_id} not found"
        )
    
    update_data = call_log_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(call_log, field, value)
    
    await db.commit()
    await db.refresh(call_log)
    
    return call_log