# Dependencies (DB, auth, etc.)

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.database.session import get_db


async def get_current_db(
    db: AsyncSession = Depends(get_db)
) -> AsyncSession:
    """Get current database session"""
    return db


# Optional: Add authentication dependency here
# async def get_current_user(...):
#     pass