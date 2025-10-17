class VAPICallRequest(BaseModel):
    driver_id: int
    phone_number: str
    driver_name: str
    priority: Optional[str] = "normal"


class VAPICallResponse(BaseModel):
    call_id: str
    status: str
    message: str


class VAPIWebhookEvent(BaseModel):
    type: str
    call: Optional[dict] = None
    function: Optional[dict] = None
    transcript: Optional[dict] = None
    message: Optional[dict] = None


class VAPIFunctionLoadedStatus(BaseModel):
    driver_id: int
    is_loaded: bool = True
    cargo_type: Optional[str] = None
    weight_lbs: Optional[float] = None
    cargo_quantity: Optional[str] = None
    destination: Optional[str] = None
    load_completed_time: Optional[str] = None
    departure_time: Optional[str] = None
    issues_notes: Optional[str] = None


class VAPIFunctionNotLoadedStatus(BaseModel):
    driver_id: int
    is_loaded: bool = False
    delay_reason_category: str
    delay_reason_details: str
    estimated_load_time: Optional[str] = None
    waiting_duration_minutes: Optional[int] = None
    trucks_in_queue: Optional[int] = None
    is_recurring_issue: Optional[bool] = False
    current_location: Optional[str] = None