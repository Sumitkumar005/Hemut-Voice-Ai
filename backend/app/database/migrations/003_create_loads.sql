CREATE TABLE IF NOT EXISTS loads (
    load_id SERIAL PRIMARY KEY,
    driver_id INTEGER REFERENCES drivers(driver_id) ON DELETE SET NULL,
    truck_id INTEGER REFERENCES trucks(truck_id) ON DELETE SET NULL,
    
    -- Load Details
    cargo_type VARCHAR(100),
    cargo_description TEXT,
    cargo_quantity VARCHAR(50),
    weight_lbs DECIMAL(10,2),
    
    -- Location & Time
    pickup_location TEXT,
    destination TEXT,
    load_completed_time TIMESTAMP WITH TIME ZONE,
    scheduled_departure_time TIMESTAMP WITH TIME ZONE,
    actual_departure_time TIMESTAMP WITH TIME ZONE,
    estimated_arrival_time TIMESTAMP WITH TIME ZONE,
    actual_arrival_time TIMESTAMP WITH TIME ZONE,
    
    -- Status
    load_status VARCHAR(30) DEFAULT 'ASSIGNED' CHECK (
        load_status IN ('ASSIGNED', 'LOADING', 'LOADED', 'IN_TRANSIT', 'DELIVERED', 'CANCELLED')
    ),
    
    -- Additional Info
    special_instructions TEXT,
    temperature_control BOOLEAN DEFAULT FALSE,
    hazmat BOOLEAN DEFAULT FALSE,
    priority_level VARCHAR(20) DEFAULT 'NORMAL' CHECK (priority_level IN ('LOW', 'NORMAL', 'HIGH', 'URGENT')),
    
    -- Financial
    rate_amount DECIMAL(10,2),
    customer_name VARCHAR(200),
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_loads_driver ON loads(driver_id);
CREATE INDEX idx_loads_truck ON loads(truck_id);
CREATE INDEX idx_loads_status ON loads(load_status);
CREATE INDEX idx_loads_created_date ON loads(created_at);

-- Create updated_at trigger
CREATE TRIGGER update_loads_updated_at
    BEFORE UPDATE ON loads
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

COMMENT ON TABLE loads IS 'Stores load/shipment information';