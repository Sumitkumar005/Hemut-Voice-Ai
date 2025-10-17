import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_driver(client: AsyncClient):
    """Test creating a new driver"""
    driver_data = {
        "driver_name": "Test Driver",
        "phone_number": "+15551234567",
        "license_number": "DL123456",
        "email": "test@example.com",
        "status": "ACTIVE"
    }
    
    response = await client.post("/api/drivers/", json=driver_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["driver_name"] == "Test Driver"
    assert data["phone_number"] == "+15551234567"
    assert "driver_id" in data


@pytest.mark.asyncio
async def test_get_drivers(client: AsyncClient):
    """Test getting all drivers"""
    response = await client.get("/api/drivers/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_driver_by_id(client: AsyncClient):
    """Test getting specific driver"""
    # First create a driver
    driver_data = {
        "driver_name": "Test Driver",
        "phone_number": "+15551234567",
        "license_number": "DL123456"
    }
    create_response = await client.post("/api/drivers/", json=driver_data)
    driver_id = create_response.json()["driver_id"]
    
    # Get the driver
    response = await client.get(f"/api/drivers/{driver_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["driver_id"] == driver_id
    assert data["driver_name"] == "Test Driver"


@pytest.mark.asyncio
async def test_update_driver(client: AsyncClient):
    """Test updating driver"""
    # Create driver
    driver_data = {
        "driver_name": "Test Driver",
        "phone_number": "+15551234567"
    }
    create_response = await client.post("/api/drivers/", json=driver_data)
    driver_id = create_response.json()["driver_id"]
    
    # Update driver
    update_data = {"driver_name": "Updated Driver"}
    response = await client.put(f"/api/drivers/{driver_id}", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["driver_name"] == "Updated Driver"


@pytest.mark.asyncio
async def test_delete_driver(client: AsyncClient):
    """Test deleting driver"""
    # Create driver
    driver_data = {
        "driver_name": "Test Driver",
        "phone_number": "+15551234567"
    }
    create_response = await client.post("/api/drivers/", json=driver_data)
    driver_id = create_response.json()["driver_id"]
    
    # Delete driver
    response = await client.delete(f"/api/drivers/{driver_id}")
    
    assert response.status_code == 204
