import httpx
from typing import Dict, Any
import logging

from app.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)


class VAPIService:
    """VAPI API integration service"""
    
    @staticmethod
    async def initiate_call(
        phone_number: str,
        driver_name: str,
        custom_variables: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Initiate outbound call via VAPI"""
        
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
                    "number": phone_number,
                    "name": driver_name
                }
            }
            
            if custom_variables:
                payload["assistant"]["variableValues"] = custom_variables
            
            try:
                response = await client.post(
                    f"{settings.VAPI_BASE_URL}/call/phone",
                    headers=headers,
                    json=payload,
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
                
            except httpx.HTTPError as e:
                logger.error(f"VAPI call failed: {str(e)}")
                raise
    
    @staticmethod
    async def get_call_status(call_id: str) -> Dict[str, Any]:
        """Get call status from VAPI"""
        
        async with httpx.AsyncClient() as client:
            headers = {
                "Authorization": f"Bearer {settings.VAPI_API_KEY}"
            }
            
            try:
                response = await client.get(
                    f"{settings.VAPI_BASE_URL}/call/{call_id}",
                    headers=headers,
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
                
            except httpx.HTTPError as e:
                logger.error(f"Failed to get call status: {str(e)}")
                raise
