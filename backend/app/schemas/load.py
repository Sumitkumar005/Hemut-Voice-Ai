from decimal import Decimal


class LoadBase(BaseModel):
    driver_id: Optional[int] = None
    truck_id: Optional[int] = None
    cargo_type: Optional[str] = None
    cargo_description: Optional[str] = None
    cargo_quantity: Optional[str] = None
    weight_lbs: Optional[Decimal] = None
    pickup_location: Optional[str] = None
    destination: Optional[str] = None
    scheduled_departure_time: Optional[datetime] = None
    load_status: Optional[str] = "ASSIGNED"
    special_instructions: Optional[str] = None
    temperature_control: Optional[bool] = False
    hazmat: Optional[bool] = False
    priority_level: Optional[str] = "NORMAL"
    rate_amount: Optional[Decimal] = None
    customer_name: Optional[str] = None


class LoadCreate(LoadBase):
    driver_id: int
    truck_id: int
    pickup_location: str
    destination: str


class LoadUpdate(BaseModel):
    cargo_type: Optional[str] = None
    cargo_description: Optional[str] = None
    cargo_quantity: Optional[str] = None
    weight_lbs: Optional[Decimal] = None
    load_status: Optional[str] = None
    load_completed_time: Optional[datetime] = None
    actual_departure_time: Optional[datetime] = None
    actual_arrival_time: Optional[datetime] = None


class LoadResponse(LoadBase):
    load_id: int
    load_completed_time: Optional[datetime]
    actual_departure_time: Optional[datetime]
    estimated_arrival_time: Optional[datetime]
    actual_arrival_time: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True