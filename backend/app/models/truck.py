from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from app.database.session import Base


class Truck(Base):
    __tablename__ = "trucks"
    
    truck_id = Column(Integer, primary_key=True, index=True)
    truck_number = Column(String(50), unique=True, nullable=False, index=True)
    truck_type = Column(String(50))
    capacity_lbs = Column(Integer)
    vin_number = Column(String(50), unique=True)
    license_plate = Column(String(20), unique=True)
    current_location = Column(String)
    status = Column(String(20), default="AVAILABLE", index=True)
    last_maintenance_date = Column(Date)
    next_maintenance_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    loads = relationship("Load", back_populates="truck")