import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_truck(client: AsyncClient):
    """Test creating a new truck"""
    truck_data = {
        "truck_number": "TRK-TEST-001",
        "truck_type": "DRY_VAN",
        "capacity_lbs": 45000,
        "vin_number": "1HGBH41JXMN109999",
        "license_plate": "IL-TEST-123",
        "status": "AVAILABLE"
    }
    
    response = await client.post("/api/trucks/", json=truck_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["truck_number"] == "TRK-TEST-001"
    assert data["truck_type"] == "DRY_VAN"


@pytest.mark.asyncio
async def test_get_trucks(client: AsyncClient):
    """Test getting all trucks"""
    response = await client.get("/api/trucks/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_filter_trucks_by_status(client: AsyncClient):
    """Test filtering trucks by status"""
    response = await client.get("/api/trucks/?status=AVAILABLE")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_filter_trucks_by_type(client: AsyncClient):
    """Test filtering trucks by type"""
    response = await client.get("/api/trucks/?truck_type=DRY_VAN")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)