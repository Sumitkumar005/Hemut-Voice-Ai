from app.models.truck import Truck
from app.schemas.truck import TruckCreate, TruckUpdate, TruckResponse

router = APIRouter()


@router.get("/", response_model=List[TruckResponse])
async def get_trucks(
    status_filter: Optional[str] = Query(None, alias="status"),
    truck_type: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all trucks with optional filters"""
    query = select(Truck)
    
    if status_filter:
        query = query.where(Truck.status == status_filter)
    if truck_type:
        query = query.where(Truck.truck_type == truck_type)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    trucks = result.scalars().all()
    
    return trucks


@router.get("/{truck_id}", response_model=TruckResponse)
async def get_truck(
    truck_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific truck by ID"""
    result = await db.execute(
        select(Truck).where(Truck.truck_id == truck_id)
    )
    truck = result.scalar_one_or_none()
    
    if not truck:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck with ID {truck_id} not found"
        )
    
    return truck


@router.post("/", response_model=TruckResponse, status_code=status.HTTP_201_CREATED)
async def create_truck(
    truck: TruckCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new truck"""
    db_truck = Truck(**truck.model_dump())
    db.add(db_truck)
    await db.commit()
    await db.refresh(db_truck)
    
    return db_truck


@router.put("/{truck_id}", response_model=TruckResponse)
async def update_truck(
    truck_id: int,
    truck_update: TruckUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update truck information"""
    result = await db.execute(
        select(Truck).where(Truck.truck_id == truck_id)
    )
    truck = result.scalar_one_or_none()
    
    if not truck:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck with ID {truck_id} not found"
        )
    
    update_data = truck_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(truck, field, value)
    
    await db.commit()
    await db.refresh(truck)
    
    return truck
