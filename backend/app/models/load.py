from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Load(Base):
    __tablename__ = "loads"
    
    load_id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.driver_id"), index=True)
    truck_id = Column(Integer, ForeignKey("trucks.truck_id"), index=True)
    
    # Load Details
    cargo_type = Column(String(100))
    cargo_description = Column(Text)
    cargo_quantity = Column(String(50))
    weight_lbs = Column(Numeric(10, 2))
    
    # Location & Time
    pickup_location = Column(Text)
    destination = Column(Text)
    load_completed_time = Column(DateTime)
    scheduled_departure_time = Column(DateTime)
    actual_departure_time = Column(DateTime)
    estimated_arrival_time = Column(DateTime)
    actual_arrival_time = Column(DateTime)
    
    # Status
    load_status = Column(String(30), default="ASSIGNED", index=True)
    
    # Additional Info
    special_instructions = Column(Text)
    temperature_control = Column(Boolean, default=False)
    hazmat = Column(Boolean, default=False)
    priority_level = Column(String(20), default="NORMAL")
    
    # Financial
    rate_amount = Column(Numeric(10, 2))
    customer_name = Column(String(200))
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    driver = relationship("Driver", back_populates="loads")
    truck = relationship("Truck", back_populates="loads")
    status_updates = relationship("StatusUpdate", back_populates="load")