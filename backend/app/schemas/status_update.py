class StatusUpdateBase(BaseModel):
    driver_id: int
    is_loaded: bool
    load_id: Optional[int] = None
    truck_id: Optional[int] = None


class StatusUpdateLoadedCreate(StatusUpdateBase):
    is_loaded: bool = True
    cargo_loaded_time: Optional[datetime] = None
    departure_time: Optional[datetime] = None
    driver_location: Optional[str] = None
    additional_notes: Optional[str] = None


class StatusUpdateNotLoadedCreate(StatusUpdateBase):
    is_loaded: bool = False
    delay_reason_category: str
    delay_reason_details: str
    estimated_load_time: Optional[datetime] = None
    waiting_duration_minutes: Optional[int] = None
    trucks_in_queue: Optional[int] = None
    is_recurring_issue: Optional[bool] = False
    driver_location: Optional[str] = None
    additional_notes: Optional[str] = None


class StatusUpdateResponse(StatusUpdateBase):
    update_id: int
    call_log_id: Optional[int]
    status_type: Optional[str]
    delay_reason_category: Optional[str]
    delay_reason_details: Optional[str]
    estimated_load_time: Optional[datetime]
    waiting_duration_minutes: Optional[int]
    trucks_in_queue: Optional[int]
    is_recurring_issue: Optional[bool]
    cargo_loaded_time: Optional[datetime]
    departure_time: Optional[datetime]
    driver_location: Optional[str]
    additional_notes: Optional[str]
    reported_at: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True