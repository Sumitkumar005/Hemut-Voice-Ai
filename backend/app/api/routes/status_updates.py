from app.models.status_update import StatusUpdate
from app.schemas.status_update import (
    StatusUpdateLoadedCreate,
    StatusUpdateNotLoadedCreate,
    StatusUpdateResponse
)

router = APIRouter()


@router.get("/", response_model=List[StatusUpdateResponse])
async def get_status_updates(
    driver_id: Optional[int] = None,
    load_id: Optional[int] = None,
    is_loaded: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all status updates with optional filters"""
    query = select(StatusUpdate)
    
    if driver_id:
        query = query.where(StatusUpdate.driver_id == driver_id)
    if load_id:
        query = query.where(StatusUpdate.load_id == load_id)
    if is_loaded is not None:
        query = query.where(StatusUpdate.is_loaded == is_loaded)
    
    query = query.order_by(StatusUpdate.reported_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    status_updates = result.scalars().all()
    
    return status_updates


@router.get("/latest")
async def get_latest_status_updates(
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    """Get latest status updates across all drivers"""
    query = select(StatusUpdate).order_by(
        StatusUpdate.reported_at.desc()
    ).limit(limit)
    
    result = await db.execute(query)
    updates = result.scalars().all()
    
    return updates


@router.post("/loaded", response_model=StatusUpdateResponse, status_code=status.HTTP_201_CREATED)
async def create_loaded_status(
    status_update: StatusUpdateLoadedCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a status update for a loaded driver"""
    db_status = StatusUpdate(
        **status_update.model_dump(),
        status_type="LOADED",
        reported_at=datetime.utcnow()
    )
    db.add(db_status)
    await db.commit()
    await db.refresh(db_status)
    
    return db_status


@router.post("/not-loaded", response_model=StatusUpdateResponse, status_code=status.HTTP_201_CREATED)
async def create_not_loaded_status(
    status_update: StatusUpdateNotLoadedCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a status update for a delayed/not loaded driver"""
    db_status = StatusUpdate(
        **status_update.model_dump(),
        status_type="NOT_LOADED",
        reported_at=datetime.utcnow()
    )
    db.add(db_status)
    await db.commit()
    await db.refresh(db_status)
    
    return db_status