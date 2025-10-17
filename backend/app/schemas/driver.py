from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime, date


class DriverBase(BaseModel):
    driver_name: str
    phone_number: str
    license_number: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[str] = "ACTIVE"
    current_truck_id: Optional[int] = None
    
    @validator('phone_number')
    def validate_phone(cls, v):
        # Simple phone validation
        import re
        phone = re.sub(r'\D', '', v)
        if len(phone) < 10:
            raise ValueError('Phone number must have at least 10 digits')
        return v


class DriverCreate(DriverBase):
    hire_date: Optional[date] = None


class DriverUpdate(BaseModel):
    driver_name: Optional[str] = None
    phone_number: Optional[str] = None
    license_number: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[str] = None
    current_truck_id: Optional[int] = None


class DriverResponse(DriverBase):
    driver_id: int
    hire_date: Optional[date]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True