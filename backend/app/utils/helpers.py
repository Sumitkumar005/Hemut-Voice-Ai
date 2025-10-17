from datetime import datetime, timedelta
from typing import Optional
import re


def format_phone_number(phone: str) -> str:
    """Format phone number to E.164 format"""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Add +1 if not present for US numbers
    if len(digits) == 10:
        return f"+1{digits}"
    elif len(digits) == 11 and digits.startswith('1'):
        return f"+{digits}"
    else:
        return f"+{digits}"


def validate_phone_number(phone: str) -> bool:
    """Validate phone number format"""
    pattern = r'^\+?1?\d{10}$'
    return bool(re.match(pattern, re.sub(r'\D', '', phone)))


def calculate_duration(start: datetime, end: datetime) -> int:
    """Calculate duration in seconds between two timestamps"""
    if not start or not end:
        return 0
    return int((end - start).total_seconds())


def estimate_arrival_time(
    distance_miles: float,
    average_speed: float = 55.0
) -> datetime:
    """Estimate arrival time based on distance"""
    hours = distance_miles / average_speed
    return datetime.utcnow() + timedelta(hours=hours)


def format_currency(amount: float) -> str:
    """Format amount as currency"""
    return f"${amount:,.2f}"


def calculate_cost_per_minute() -> float:
    """Calculate cost per minute of delay (industry standard ~$1/min)"""
    return 1.0


def get_time_of_day() -> str:
    """Get current time of day category"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "MORNING"
    elif 12 <= hour < 17:
        return "AFTERNOON"
    elif 17 <= hour < 21:
        return "EVENING"
    else:
        return "NIGHT"


def is_business_hours() -> bool:
    """Check if current time is business hours (7 AM - 7 PM)"""
    hour = datetime.now().hour
    return 7 <= hour < 19