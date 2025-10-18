import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.driver import Driver
from app.models.truck import Truck


@pytest.mark.asyncio
async def test_create_load(client: AsyncClient, db_session: AsyncSession):
    """Test creating a new load"""
    # Create driver first
    driver = Driver(
        driver_name="Test Driver",
        phone_number="+15551234567",
        status="ACTIVE"
    )
    db_session.add(driver)
    
    # Create truck
    truck = Truck(
        truck_number="TRK-TEST-001",
        truck_type="DRY_VAN",
        capacity_lbs=45000,
        status="AVAILABLE"
    )
    db_session.add(truck)
    await db_session.commit()
    await db_session.refresh(driver)
    await db_session.refresh(truck)
    
    # Create load
    load_data = {
        "driver_id": driver.driver_id,
        "truck_id": truck.truck_id,
        "pickup_location": "Chicago Warehouse",
        "destination": "Dallas Distribution Center",
        "cargo_type": "Electronics",
        "weight_lbs": 35000.0,
        "load_status": "ASSIGNED"
    }
    
    response = await client.post("/api/loads/", json=load_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["driver_id"] == driver.driver_id
    assert data["truck_id"] == truck.truck_id
    assert data["pickup_location"] == "Chicago Warehouse"
    assert "load_id" in data


@pytest.mark.asyncio
async def test_get_loads(client: AsyncClient):
    """Test getting all loads"""
    response = await client.get("/api/loads/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_load_by_id(client: AsyncClient, db_session: AsyncSession):
    """Test getting specific load"""
    # Create test data
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    truck = Truck(truck_number="TRK-001", status="AVAILABLE")
    db_session.add_all([driver, truck])
    await db_session.commit()
    
    # Create load
    from app.models.load import Load
    load = Load(
        driver_id=driver.driver_id,
        truck_id=truck.truck_id,
        pickup_location="Test Location",
        destination="Test Destination",
        load_status="ASSIGNED"
    )
    db_session.add(load)
    await db_session.commit()
    await db_session.refresh(load)
    
    # Get load
    response = await client.get(f"/api/loads/{load.load_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["load_id"] == load.load_id


@pytest.mark.asyncio
async def test_update_load_status(client: AsyncClient, db_session: AsyncSession):
    """Test updating load status"""
    # Create test load
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    truck = Truck(truck_number="TRK-001", status="AVAILABLE")
    db_session.add_all([driver, truck])
    await db_session.commit()
    
    from app.models.load import Load
    load = Load(
        driver_id=driver.driver_id,
        truck_id=truck.truck_id,
        pickup_location="Test",
        destination="Test",
        load_status="ASSIGNED"
    )
    db_session.add(load)
    await db_session.commit()
    await db_session.refresh(load)
    
    # Update status
    response = await client.put(
        f"/api/loads/{load.load_id}/status",
        params={"new_status": "LOADED"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["new_status"] == "LOADED"


@pytest.mark.asyncio
async def test_filter_loads_by_driver(client: AsyncClient, db_session: AsyncSession):
    """Test filtering loads by driver"""
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    truck = Truck(truck_number="TRK-001", status="AVAILABLE")
    db_session.add_all([driver, truck])
    await db_session.commit()
    
    from app.models.load import Load
    load = Load(
        driver_id=driver.driver_id,
        truck_id=truck.truck_id,
        pickup_location="Test",
        destination="Test"
    )
    db_session.add(load)
    await db_session.commit()
    
    # Filter by driver
    response = await client.get(f"/api/loads/?driver_id={driver.driver_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert all(l["driver_id"] == driver.driver_id for l in data)


@pytest.mark.asyncio
async def test_filter_loads_by_status(client: AsyncClient):
    """Test filtering loads by status"""
    response = await client.get("/api/loads/?status=ASSIGNED")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)