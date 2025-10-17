import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import AsyncSessionLocal
from app.models.driver import Driver
from app.models.truck import Truck
from app.models.load import Load
from datetime import datetime, timedelta


async def seed_data():
    """Seed database with sample data"""
    
    async with AsyncSessionLocal() as session:
        print("🌱 Seeding database...")
        
        # Create drivers
        drivers = [
            Driver(
                driver_name="John Smith",
                phone_number="+15551234567",
                license_number="DL001234",
                email="john@example.com",
                status="ACTIVE"
            ),
            Driver(
                driver_name="Sarah Johnson",
                phone_number="+15551234568",
                license_number="DL001235",
                email="sarah@example.com",
                status="ACTIVE"
            ),
            Driver(
                driver_name="Mike Davis",
                phone_number="+15551234569",
                license_number="DL001236",
                email="mike@example.com",
                status="ACTIVE"
            )
        ]
        
        session.add_all(drivers)
        await session.commit()
        print(f"✅ Created {len(drivers)} drivers")
        
        # Create trucks
        trucks = [
            Truck(
                truck_number="TRK-001",
                truck_type="DRY_VAN",
                capacity_lbs=45000,
                status="AVAILABLE"
            ),
            Truck(
                truck_number="TRK-002",
                truck_type="REFRIGERATED",
                capacity_lbs=40000,
                status="AVAILABLE"
            ),
            Truck(
                truck_number="TRK-003",
                truck_type="FLATBED",
                capacity_lbs=48000,
                status="AVAILABLE"
            )
        ]
        
        session.add_all(trucks)
        await session.commit()
        print(f"✅ Created {len(trucks)} trucks")
        
        print("🎉 Database seeding completed!")


if __name__ == "__main__":
    asyncio.run(seed_data())