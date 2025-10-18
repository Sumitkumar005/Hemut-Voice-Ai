from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional

from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverUpdate


class DriverService:
    """Driver business logic service"""
    
    @staticmethod
    async def get_all_drivers(
        db: AsyncSession,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Driver]:
        """Get all drivers with filters"""
        query = select(Driver)
        
        if status:
            query = query.where(Driver.status == status)
        
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def get_driver_by_id(db: AsyncSession, driver_id: int) -> Optional[Driver]:
        """Get driver by ID"""
        result = await db.execute(
            select(Driver).where(Driver.driver_id == driver_id)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create_driver(db: AsyncSession, driver: DriverCreate) -> Driver:
        """Create new driver"""
        db_driver = Driver(**driver.model_dump())
        db.add(db_driver)
        await db.commit()
        await db.refresh(db_driver)
        return db_driver
    
    @staticmethod
    async def update_driver(
        db: AsyncSession,
        driver_id: int,
        driver_update: DriverUpdate
    ) -> Optional[Driver]:
        """Update driver"""
        driver = await DriverService.get_driver_by_id(db, driver_id)
        if not driver:
            return None
        
        update_data = driver_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(driver, field, value)
        
        await db.commit()
        await db.refresh(driver)
        return driver