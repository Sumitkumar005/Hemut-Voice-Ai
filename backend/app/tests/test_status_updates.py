import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from app.models.driver import Driver


@pytest.mark.asyncio
async def test_create_loaded_status(client: AsyncClient, db_session: AsyncSession):
    """Test creating loaded status update"""
    # Create driver
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    db_session.add(driver)
    await db_session.commit()
    await db_session.refresh(driver)
    
    # Create status update
    status_data = {
        "driver_id": driver.driver_id,
        "is_loaded": True,
        "cargo_loaded_time": datetime.utcnow().isoformat(),
        "departure_time": datetime.utcnow().isoformat(),
        "driver_location": "Chicago Warehouse",
        "additional_notes": "All cargo secured"
    }
    
    response = await client.post("/api/status-updates/loaded", json=status_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["is_loaded"] == True
    assert data["driver_id"] == driver.driver_id


@pytest.mark.asyncio
async def test_create_not_loaded_status(client: AsyncClient, db_session: AsyncSession):
    """Test creating not loaded status update"""
    # Create driver
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    db_session.add(driver)
    await db_session.commit()
    await db_session.refresh(driver)
    
    # Create status update
    status_data = {
        "driver_id": driver.driver_id,
        "is_loaded": False,
        "delay_reason_category": "WAREHOUSE_DELAY",
        "delay_reason_details": "Long queue at warehouse dock",
        "waiting_duration_minutes": 90,
        "trucks_in_queue": 5,
        "is_recurring_issue": True,
        "driver_location": "ABC Warehouse"
    }
    
    response = await client.post("/api/status-updates/not-loaded", json=status_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["is_loaded"] == False
    assert data["delay_reason_category"] == "WAREHOUSE_DELAY"


@pytest.mark.asyncio
async def test_get_status_updates(client: AsyncClient):
    """Test getting all status updates"""
    response = await client.get("/api/status-updates/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_latest_status_updates(client: AsyncClient):
    """Test getting latest status updates"""
    response = await client.get("/api/status-updates/latest?limit=10")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)