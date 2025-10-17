from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.database.session import Base


class DriverStatusEnum(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ON_LEAVE = "ON_LEAVE"


class Driver(Base):
    __tablename__ = "drivers"
    
    driver_id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False, index=True)
    license_number = Column(String(50), unique=True)
    email = Column(String(100))
    status = Column(String(20), default="ACTIVE", index=True)
    current_truck_id = Column(Integer)
    hire_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    loads = relationship("Load", back_populates="driver")
    status_updates = relationship("StatusUpdate", back_populates="driver")
    call_logs = relationship("CallLog", back_populates="driver")