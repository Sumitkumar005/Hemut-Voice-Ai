class CallLogBase(BaseModel):
    driver_id: int
    phone_number: str
    call_direction: Optional[str] = "OUTBOUND"
    call_status: Optional[str] = "INITIATED"


class CallLogCreate(CallLogBase):
    call_sid: Optional[str] = None
    vapi_assistant_id: Optional[str] = None


class CallLogUpdate(BaseModel):
    call_status: Optional[str] = None
    call_answered_at: Optional[datetime] = None
    call_ended_at: Optional[datetime] = None
    call_duration_seconds: Optional[int] = None
    call_transcript: Optional[str] = None
    call_summary: Optional[str] = None
    call_recording_url: Optional[str] = None
    ai_confidence_score: Optional[Decimal] = None
    sentiment: Optional[str] = None
    error_message: Optional[str] = None


class CallLogResponse(CallLogBase):
    call_id: int
    call_sid: Optional[str]
    call_initiated_at: Optional[datetime]
    call_answered_at: Optional[datetime]
    call_ended_at: Optional[datetime]
    call_duration_seconds: Optional[int]
    call_transcript: Optional[str]
    call_summary: Optional[str]
    ai_confidence_score: Optional[Decimal]
    sentiment: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True