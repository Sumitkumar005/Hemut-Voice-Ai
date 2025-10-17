class CallLog(Base):
    __tablename__ = "call_logs"
    
    call_id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.driver_id"), index=True)
    
    # Call Details
    call_sid = Column(String(100), unique=True, index=True)
    phone_number = Column(String(20), nullable=False)
    call_direction = Column(String(10), default="OUTBOUND")
    call_status = Column(String(20), default="INITIATED", index=True)
    
    # Timing
    call_initiated_at = Column(DateTime)
    call_answered_at = Column(DateTime)
    call_ended_at = Column(DateTime)
    call_duration_seconds = Column(Integer)
    
    # Content
    call_transcript = Column(Text)
    call_summary = Column(Text)
    call_recording_url = Column(Text)
    
    # AI Performance
    ai_confidence_score = Column(Numeric(3, 2))
    sentiment = Column(String(20))
    
    # Metadata
    vapi_assistant_id = Column(String(100))
    error_message = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    driver = relationship("Driver", back_populates="call_logs")
    status_updates = relationship("StatusUpdate", back_populates="call_log")