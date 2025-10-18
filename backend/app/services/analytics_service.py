from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from datetime import datetime, timedelta
from typing import Dict, Any

from app.models.driver import Driver
from app.models.load import Load
from app.models.call_log import CallLog
from app.models.status_update import StatusUpdate


class AnalyticsService:
    """Analytics calculation service"""
    
    @staticmethod
    async def calculate_driver_efficiency(
        db: AsyncSession,
        driver_id: int,
        days: int = 30
    ) -> Dict[str, Any]:
        """Calculate driver efficiency metrics"""
        
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Total loads assigned
        total_loads_result = await db.execute(
            select(func.count(Load.load_id)).where(
                Load.driver_id == driver_id,
                Load.created_at >= start_date
            )
        )
        total_loads = total_loads_result.scalar() or 0
        
        # Completed loads
        completed_result = await db.execute(
            select(func.count(Load.load_id)).where(
                Load.driver_id == driver_id,
                Load.load_status == "DELIVERED",
                Load.created_at >= start_date
            )
        )
        completed_loads = completed_result.scalar() or 0
        
        # Calculate efficiency
        efficiency = (completed_loads / total_loads * 100) if total_loads > 0 else 0
        
        return {
            "driver_id": driver_id,
            "total_loads": total_loads,
            "completed_loads": completed_loads,
            "efficiency_percentage": round(efficiency, 2),
            "period_days": days
        }
    
    @staticmethod
    async def calculate_delay_costs(
        db: AsyncSession,
        days: int = 30
    ) -> Dict[str, Any]:
        """Calculate total delay costs"""
        
        start_date = datetime.utcnow() - timedelta(days=days)
        
        result = await db.execute(
            select(func.sum(StatusUpdate.waiting_duration_minutes)).where(
                StatusUpdate.is_loaded == False,
                StatusUpdate.reported_at >= start_date
            )
        )
        total_wait_minutes = result.scalar() or 0
        
        # Cost per minute ($1/minute industry standard)
        cost_per_minute = 1.0
        total_cost = total_wait_minutes * cost_per_minute
        
        return {
            "total_delay_minutes": int(total_wait_minutes),
            "total_delay_hours": round(total_wait_minutes / 60, 2),
            "estimated_cost": round(total_cost, 2),
            "period_days": days
        }
