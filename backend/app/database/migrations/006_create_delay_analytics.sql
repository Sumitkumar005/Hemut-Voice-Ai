CREATE TABLE IF NOT EXISTS delay_analytics (
    analytics_id SERIAL PRIMARY KEY,
    
    -- Pattern Analysis
    delay_category VARCHAR(50),
    location VARCHAR(200),
    warehouse_name VARCHAR(100),
    frequency_count INTEGER DEFAULT 1,
    average_delay_minutes INTEGER,
    total_delay_minutes INTEGER DEFAULT 0,
    
    -- Time Patterns
    day_of_week INTEGER CHECK (day_of_week >= 1 AND day_of_week <= 7),
    hour_of_day INTEGER CHECK (hour_of_day >= 0 AND hour_of_day <= 23),
    
    -- Cost Impact (estimated at $1 per minute delay)
    estimated_cost_impact DECIMAL(10,2),
    
    -- Related IDs for drill-down
    related_status_update_ids INTEGER[],
    
    first_occurrence TIMESTAMP WITH TIME ZONE,
    last_occurrence TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_delay_analytics_category ON delay_analytics(delay_category);
CREATE INDEX idx_delay_analytics_location ON delay_analytics(location);
CREATE INDEX idx_delay_analytics_frequency ON delay_analytics(frequency_count DESC);

-- Create updated_at trigger
CREATE TRIGGER update_delay_analytics_updated_at
    BEFORE UPDATE ON delay_analytics
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

COMMENT ON TABLE delay_analytics IS 'Aggregated analytics for delay patterns';