import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_dashboard_stats(client: AsyncClient):
    """Test getting dashboard statistics"""
    response = await client.get("/api/analytics/dashboard")
    
    assert response.status_code == 200
    data = response.json()
    
    # Check all required fields
    assert "total_drivers" in data
    assert "drivers_loaded" in data
    assert "drivers_not_loaded" in data
    assert "drivers_pending" in data
    assert "total_calls_today" in data
    assert "delays_today" in data
    assert "total_loads_active" in data


@pytest.mark.asyncio
async def test_get_delay_analytics(client: AsyncClient):
    """Test getting delay analytics"""
    response = await client.get("/api/analytics/delays?days=30")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_driver_performance(client: AsyncClient, db_session: AsyncSession):
    """Test getting driver performance metrics"""
    # Create test driver
    from app.models.driver import Driver
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    db_session.add(driver)
    await db_session.commit()
    await db_session.refresh(driver)
    
    response = await client.get(
        f"/api/analytics/driver-performance/{driver.driver_id}?days=30"
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "driver_id" in data
    assert "total_loads" in data
    assert "delay_count" in data


@pytest.mark.asyncio
async def test_get_delay_trends(client: AsyncClient):
    """Test getting delay trends"""
    response = await client.get("/api/analytics/delay-trends?days=30")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_top_delay_locations(client: AsyncClient):
    """Test getting top delay locations"""
    response = await client.get("/api/analytics/top-delay-locations?limit=10")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)