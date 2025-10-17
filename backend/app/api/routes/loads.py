from app.models.load import Load
from app.schemas.load import LoadCreate, LoadUpdate, LoadResponse
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[LoadResponse])
async def get_loads(
    status_filter: Optional[str] = Query(None, alias="status"),
    driver_id: Optional[int] = None,
    truck_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all loads with optional filters"""
    query = select(Load)
    
    if status_filter:
        query = query.where(Load.load_status == status_filter)
    if driver_id:
        query = query.where(Load.driver_id == driver_id)
    if truck_id:
        query = query.where(Load.truck_id == truck_id)
    
    query = query.order_by(Load.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    loads = result.scalars().all()
    
    return loads


@router.get("/{load_id}", response_model=LoadResponse)
async def get_load(
    load_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific load by ID"""
    result = await db.execute(
        select(Load).where(Load.load_id == load_id)
    )
    load = result.scalar_one_or_none()
    
    if not load:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Load with ID {load_id} not found"
        )
    
    return load


@router.post("/", response_model=LoadResponse, status_code=status.HTTP_201_CREATED)
async def create_load(
    load: LoadCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new load assignment"""
    # Verify driver exists
    driver_result = await db.execute(
        select(Driver).where(Driver.driver_id == load.driver_id)
    )
    if not driver_result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with ID {load.driver_id} not found"
        )
    
    # Verify truck exists
    truck_result = await db.execute(
        select(Truck).where(Truck.truck_id == load.truck_id)
    )
    if not truck_result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck with ID {load.truck_id} not found"
        )
    
    db_load = Load(**load.model_dump())
    db.add(db_load)
    await db.commit()
    await db.refresh(db_load)
    
    return db_load


@router.put("/{load_id}", response_model=LoadResponse)
async def update_load(
    load_id: int,
    load_update: LoadUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update load information"""
    result = await db.execute(
        select(Load).where(Load.load_id == load_id)
    )
    load = result.scalar_one_or_none()
    
    if not load:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Load with ID {load_id} not found"
        )
    
    update_data = load_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(load, field, value)
    
    await db.commit()
    await db.refresh(load)
    
    return load


@router.put("/{load_id}/status")
async def update_load_status(
    load_id: int,
    new_status: str,
    db: AsyncSession = Depends(get_db)
):
    """Update only the load status"""
    result = await db.execute(
        select(Load).where(Load.load_id == load_id)
    )
    load = result.scalar_one_or_none()
    
    if not load:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Load with ID {load_id} not found"
        )
    
    load.load_status = new_status
    await db.commit()
    
    return {"message": "Load status updated", "load_id": load_id, "new_status": new_status}