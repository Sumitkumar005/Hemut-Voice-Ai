from pydantic import validator
from typing import Any


class PhoneNumberValidator:
    """Phone number validation"""
    
    @staticmethod
    def validate(value: str) -> str:
        if not validate_phone_number(value):
            raise ValueError("Invalid phone number format")
        return format_phone_number(value)


class WeightValidator:
    """Weight validation"""
    
    @staticmethod
    def validate(value: float) -> float:
        if value <= 0:
            raise ValueError("Weight must be greater than 0")
        if value > 80000:  # Max legal weight in lbs
            raise ValueError("Weight exceeds maximum legal limit (80,000 lbs)")
        return value


class VINValidator:
    """VIN number validation"""
    
    @staticmethod
    def validate(value: str) -> str:
        if len(value) != 17:
            raise ValueError("VIN must be 17 characters")
        if not value.isalnum():
            raise ValueError("VIN must be alphanumeric")
        return value.upper()
