class DashboardStats(BaseModel):
    total_drivers: int
    drivers_loaded: int
    drivers_not_loaded: int
    drivers_pending: int
    total_calls_today: int
    completed_calls_today: int
    average_call_duration: Optional[int]
    delays_today: int
    total_loads_active: int


class DelayStats(BaseModel):
    delay_reason_category: str
    delay_count: int
    avg_wait_minutes: Optional[float]
    total_wait_minutes: Optional[int]
    recurring_issues: int


class DriverPerformance(BaseModel):
    driver_id: int
    driver_name: str
    total_loads: int
    loads_completed: int
    average_load_time_minutes: Optional[float]
    delay_count: int
    on_time_percentage: float


class DelayAnalyticsResponse(BaseModel):
    analytics_id: int
    delay_category: str
    location: Optional[str]
    warehouse_name: Optional[str]
    frequency_count: int
    average_delay_minutes: Optional[int]
    total_delay_minutes: int
    estimated_cost_impact: Optional[Decimal]
    first_occurrence: Optional[datetime]
    last_occurrence: Optional[datetime]
    
    class Config:
        from_attributes = True