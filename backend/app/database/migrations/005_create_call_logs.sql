CREATE TABLE IF NOT EXISTS status_updates (
    update_id SERIAL PRIMARY KEY,
    call_log_id INTEGER REFERENCES call_logs(call_id) ON DELETE CASCADE,
    driver_id INTEGER REFERENCES drivers(driver_id) ON DELETE CASCADE,
    truck_id INTEGER REFERENCES trucks(truck_id) ON DELETE SET NULL,
    load_id INTEGER REFERENCES loads(load_id) ON DELETE SET NULL,
    
    -- Status Info
    is_loaded BOOLEAN NOT NULL,
    status_type VARCHAR(30) CHECK (status_type IN ('LOADED', 'NOT_LOADED', 'DELAYED', 'ISSUE')),
    
    -- If NOT LOADED
    delay_reason_category VARCHAR(50) CHECK (
        delay_reason_category IN (
            'WAREHOUSE_DELAY', 'MECHANICAL_ISSUE', 'WEATHER', 
            'PAPERWORK', 'TRAFFIC', 'LOADING_EQUIPMENT', 'DRIVER_UNAVAILABLE', 'OTHER'
        )
    ),
    delay_reason_details TEXT,
    estimated_load_time TIMESTAMP WITH TIME ZONE,
    waiting_duration_minutes INTEGER,
    trucks_in_queue INTEGER,
    is_recurring_issue BOOLEAN DEFAULT FALSE,
    
    -- If LOADED
    cargo_loaded_time TIMESTAMP WITH TIME ZONE,
    departure_time TIMESTAMP WITH TIME ZONE,
    
    -- Common Fields
    driver_location TEXT,
    additional_notes TEXT,
    reported_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_status_updates_driver ON status_updates(driver_id);
CREATE INDEX idx_status_updates_load ON status_updates(load_id);
CREATE INDEX idx_status_updates_is_loaded ON status_updates(is_loaded);
CREATE INDEX idx_status_updates_delay_category ON status_updates(delay_reason_category);
CREATE INDEX idx_status_updates_reported ON status_updates(reported_at);

COMMENT ON TABLE status_updates IS 'Stores all status updates from driver calls';
