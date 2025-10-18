from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional

from app.models.load import Load
from app.schemas.load import LoadCreate, LoadUpdate


class LoadService:
    """Load business logic service"""
    
    @staticmethod
    async def get_all_loads(
        db: AsyncSession,
        status: Optional[str] = None,
        driver_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Load]:
        """Get all loads with filters"""
        query = select(Load)
        
        if status:
            query = query.where(Load.load_status == status)
        if driver_id:
            query = query.where(Load.driver_id == driver_id)
        
        query = query.order_by(Load.created_at.desc()).offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def get_load_by_id(db: AsyncSession, load_id: int) -> Optional[Load]:
        """Get load by ID"""
        result = await db.execute(
            select(Load).where(Load.load_id == load_id)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create_load(db: AsyncSession, load: LoadCreate) -> Load:
        """Create new load"""
        db_load = Load(**load.model_dump())
        db.add(db_load)
        await db.commit()
        await db.refresh(db_load)
        return db_load
    
    @staticmethod
    async def update_load_status(
        db: AsyncSession,
        load_id: int,
        new_status: str
    ) -> Optional[Load]:
        """Update load status"""
        load = await LoadService.get_load_by_id(db, load_id)
        if not load:
            return None
        
        load.load_status = new_status
        await db.commit()
        await db.refresh(load)
        return load
