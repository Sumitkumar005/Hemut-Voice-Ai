class TruckBase(BaseModel):
    truck_number: str
    truck_type: Optional[str] = None
    capacity_lbs: Optional[int] = None
    vin_number: Optional[str] = None
    license_plate: Optional[str] = None
    current_location: Optional[str] = None
    status: Optional[str] = "AVAILABLE"


class TruckCreate(TruckBase):
    last_maintenance_date: Optional[date] = None
    next_maintenance_date: Optional[date] = None


class TruckUpdate(BaseModel):
    truck_number: Optional[str] = None
    truck_type: Optional[str] = None
    capacity_lbs: Optional[int] = None
    current_location: Optional[str] = None
    status: Optional[str] = None
    last_maintenance_date: Optional[date] = None
    next_maintenance_date: Optional[date] = None


class TruckResponse(TruckBase):
    truck_id: int
    last_maintenance_date: Optional[date]
    next_maintenance_date: Optional[date]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True