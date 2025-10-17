CREATE TABLE IF NOT EXISTS trucks (
    truck_id SERIAL PRIMARY KEY,
    truck_number VARCHAR(50) UNIQUE NOT NULL,
    truck_type VARCHAR(50) CHECK (truck_type IN ('FLATBED', 'REFRIGERATED', 'DRY_VAN', 'TANKER', 'LOWBOY')),
    capacity_lbs INTEGER,
    vin_number VARCHAR(50) UNIQUE,
    license_plate VARCHAR(20) UNIQUE,
    current_location TEXT,
    status VARCHAR(20) DEFAULT 'AVAILABLE' CHECK (status IN ('AVAILABLE', 'IN_TRANSIT', 'MAINTENANCE', 'OUT_OF_SERVICE')),
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_trucks_status ON trucks(status);
CREATE INDEX idx_trucks_type ON trucks(truck_type);
CREATE INDEX idx_trucks_number ON trucks(truck_number);

-- Create updated_at trigger
CREATE TRIGGER update_trucks_updated_at
    BEFORE UPDATE ON trucks
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

COMMENT ON TABLE trucks IS 'Stores truck/vehicle information';