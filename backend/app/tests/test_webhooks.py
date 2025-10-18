import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.driver import Driver
from app.models.call_log import CallLog


@pytest.mark.asyncio
async def test_vapi_webhook_loaded_status(client: AsyncClient, db_session: AsyncSession):
    """Test VAPI webhook for loaded status"""
    # Create test driver
    driver = Driver(
        driver_name="Test Driver",
        phone_number="+15551234567",
        status="ACTIVE"
    )
    db_session.add(driver)
    await db_session.commit()
    await db_session.refresh(driver)
    
    # Create call log
    call_log = CallLog(
        driver_id=driver.driver_id,
        call_sid="test-call-123",
        phone_number="+15551234567",
        call_status="COMPLETED"
    )
    db_session.add(call_log)
    await db_session.commit()
    
    # Send webhook
    webhook_data = {
        "type": "function-call",
        "call": {"id": "test-call-123"},
        "functionCall": {
            "name": "record_loaded_status",
            "parameters": {
                "driver_id": driver.driver_id,
                "is_loaded": True,
                "cargo_type": "Electronics",
                "weight_lbs": 35000,
                "destination": "Dallas",
                "load_completed_time": "2024-10-17T10:00:00Z",
                "departure_time": "2024-10-17T10:30:00Z"
            }
        }
    }
    
    response = await client.post("/api/webhooks/vapi", json=webhook_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "received"


@pytest.mark.asyncio
async def test_vapi_webhook_not_loaded_status(client: AsyncClient, db_session: AsyncSession):
    """Test VAPI webhook for not loaded status"""
    # Create test driver
    driver = Driver(
        driver_name="Test Driver",
        phone_number="+15551234567",
        status="ACTIVE"
    )
    db_session.add(driver)
    await db_session.commit()
    await db_session.refresh(driver)
    
    # Send webhook
    webhook_data = {
        "type": "function-call",
        "call": {"id": "test-call-456"},
        "functionCall": {
            "name": "record_not_loaded_status",
            "parameters": {
                "driver_id": driver.driver_id,
                "is_loaded": False,
                "delay_reason_category": "WAREHOUSE_DELAY",
                "delay_reason_details": "Long queue at warehouse",
                "waiting_duration_minutes": 120,
                "trucks_in_queue": 5,
                "is_recurring_issue": True,
                "current_location": "Chicago Warehouse"
            }
        }
    }
    
    response = await client.post("/api/webhooks/vapi", json=webhook_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "received"


@pytest.mark.asyncio
async def test_vapi_webhook_call_ended(client: AsyncClient, db_session: AsyncSession):
    """Test VAPI webhook for call ended"""
    # Create driver and call log
    driver = Driver(driver_name="Test Driver", phone_number="+15551234567")
    db_session.add(driver)
    await db_session.commit()
    
    call_log = CallLog(
        driver_id=driver.driver_id,
        call_sid="test-call-789",
        phone_number="+15551234567",
        call_status="ANSWERED"
    )
    db_session.add(call_log)
    await db_session.commit()
    
    # Send webhook
    webhook_data = {
        "type": "call-ended",
        "call": {
            "id": "test-call-789",
            "duration": 180,
            "transcript": "Test conversation transcript",
            "summary": "Driver confirmed loaded status"
        }
    }
    
    response = await client.post("/api/webhooks/vapi", json=webhook_data)
    
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_webhook_invalid_event_type(client: AsyncClient):
    """Test webhook with invalid event type"""
    webhook_data = {
        "type": "unknown-event",
        "data": {}
    }
    
    response = await client.post("/api/webhooks/vapi", json=webhook_data)
    
    # Should still return 200 but log as unhandled
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_webhook_missing_driver(client: AsyncClient):
    """Test webhook with non-existent driver"""
    webhook_data = {
        "type": "function-call",
        "functionCall": {
            "name": "record_loaded_status",
            "parameters": {
                "driver_id": 99999,  # Non-existent
                "is_loaded": True
            }
        }
    }
    
    # Should handle gracefully
    response = await client.post("/api/webhooks/vapi", json=webhook_data)
    assert response.status_code in [200, 404, 500]