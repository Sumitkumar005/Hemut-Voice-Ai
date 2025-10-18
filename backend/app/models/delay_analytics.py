from sqlalchemy import Column, Integer, String, Numeric, DateTime, ARRAY
from datetime import datetime

from app.database.session import Base


class DelayAnalytics(Base):
    __tablename__ = "delay_analytics"
    
    analytics_id = Column(Integer, primary_key=True, index=True)
    
    # Pattern Analysis
    delay_category = Column(String(50), index=True)
    location = Column(String(200), index=True)
    warehouse_name = Column(String(100))
    frequency_count = Column(Integer, default=1, index=True)
    average_delay_minutes = Column(Integer)
    total_delay_minutes = Column(Integer, default=0)
    
    # Time Patterns
    day_of_week = Column(Integer)  # 1-7 (Monday-Sunday)
    hour_of_day = Column(Integer)  # 0-23
    
    # Cost Impact
    estimated_cost_impact = Column(Numeric(10, 2))
    
    # Related IDs
    related_status_update_ids = Column(ARRAY(Integer))
    
    # Timestamps
    first_occurrence = Column(DateTime)
    last_occurrence = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)