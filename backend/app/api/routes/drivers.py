from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Optional

from app.database.session import get_db
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverUpdate, DriverResponse

router = APIRouter()


@router.get("/", response_model=List[DriverResponse])
async def get_drivers(
    status_filter: Optional[str] = Query(None, alias="status"),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all drivers with optional status filter"""
    query = select(Driver)
    
    if status_filter:
        query = query.where(Driver.status == status_filter)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    drivers = result.scalars().all()
    
    return drivers


@router.get("/{driver_id}", response_model=DriverResponse)
async def get_driver(
    driver_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific driver by ID"""
    result = await db.execute(
        select(Driver).where(Driver.driver_id == driver_id)
    )
    driver = result.scalar_one_or_none()
    
    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with ID {driver_id} not found"
        )
    
    return driver


@router.post("/", response_model=DriverResponse, status_code=status.HTTP_201_CREATED)
async def create_driver(
    driver: DriverCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new driver"""
    # Check if phone number already exists
    existing = await db.execute(
        select(Driver).where(Driver.phone_number == driver.phone_number)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone number already registered"
        )
    
    db_driver = Driver(**driver.model_dump())
    db.add(db_driver)
    await db.commit()
    await db.refresh(db_driver)
    
    return db_driver


@router.put("/{driver_id}", response_model=DriverResponse)
async def update_driver(
    driver_id: int,
    driver_update: DriverUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update driver information"""
    result = await db.execute(
        select(Driver).where(Driver.driver_id == driver_id)
    )
    driver = result.scalar_one_or_none()
    
    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with ID {driver_id} not found"
        )
    
    # Update only provided fields
    update_data = driver_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(driver, field, value)
    
    await db.commit()
    await db.refresh(driver)
    
    return driver


@router.delete("/{driver_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_driver(
    driver_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a driver"""
    result = await db.execute(
        select(Driver).where(Driver.driver_id == driver_id)
    )
    driver = result.scalar_one_or_none()
    
    if not driver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with ID {driver_id} not found"
        )
    
    await db.delete(driver)
    await db.commit()
    
    return None
