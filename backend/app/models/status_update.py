class StatusUpdate(Base):
    __tablename__ = "status_updates"
    
    update_id = Column(Integer, primary_key=True, index=True)
    call_log_id = Column(Integer, ForeignKey("call_logs.call_id"))
    driver_id = Column(Integer, ForeignKey("drivers.driver_id"), index=True)
    truck_id = Column(Integer, ForeignKey("trucks.truck_id"))
    load_id = Column(Integer, ForeignKey("loads.load_id"), index=True)
    
    # Status Info
    is_loaded = Column(Boolean, nullable=False, index=True)
    status_type = Column(String(30))
    
    # If NOT LOADED
    delay_reason_category = Column(String(50), index=True)
    delay_reason_details = Column(Text)
    estimated_load_time = Column(DateTime)
    waiting_duration_minutes = Column(Integer)
    trucks_in_queue = Column(Integer)
    is_recurring_issue = Column(Boolean, default=False)
    
    # If LOADED
    cargo_loaded_time = Column(DateTime)
    departure_time = Column(DateTime)
    
    # Common Fields
    driver_location = Column(Text)
    additional_notes = Column(Text)
    reported_at = Column(DateTime, default=datetime.utcnow, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    call_log = relationship("CallLog", back_populates="status_updates")
    driver = relationship("Driver", back_populates="status_updates")
    load = relationship("Load", back_populates="status_updates")