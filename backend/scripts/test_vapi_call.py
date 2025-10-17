import asyncio
import httpx
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings

settings = get_settings()


async def test_vapi_call():
    """Test making a VAPI call"""
    
    print("📞 Testing VAPI call integration...")
    
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {settings.VAPI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "assistant": {
                "assistantId": settings.VAPI_ASSISTANT_ID
            },
            "phoneNumberId": settings.VAPI_PHONE_NUMBER_ID,
            "customer": {
                "number": "+15551234567",  # Test number
                "name": "Test Driver"
            }
        }
        
        try:
            response = await client.post(
                f"{settings.VAPI_BASE_URL}/call/phone",
                headers=headers,
                json=payload,
                timeout=10.0
            )
            
            response.raise_for_status()
            data = response.json()
            
            print("✅ VAPI call initiated successfully!")
            print(f"   Call ID: {data.get('id')}")
            print(f"   Status: {data.get('status')}")
            
        except httpx.HTTPError as e:
            print(f"❌ VAPI call failed: {str(e)}")
            if hasattr(e, 'response'):
                print(f"   Response: {e.response.text}")


if __name__ == "__main__":
    asyncio.run(test_vapi_call())