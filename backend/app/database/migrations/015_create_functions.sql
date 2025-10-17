-- ============================================================================
-- MIGRATION 015: CREATE FUNCTIONS FOR ANALYTICS
-- ============================================================================

-- Function: Get Dashboard Statistics
CREATE OR REPLACE FUNCTION get_dashboard_stats()
RETURNS JSON AS $$
DECLARE
    result JSON;
BEGIN
    SELECT json_build_object(
        'total_drivers', (SELECT COUNT(*) FROM drivers WHERE status = 'ACTIVE'),
        'drivers_loaded', (SELECT COUNT(DISTINCT driver_id) FROM status_updates 
                          WHERE is_loaded = TRUE AND DATE(reported_at) = CURRENT_DATE),
        'drivers_not_loaded', (SELECT COUNT(DISTINCT driver_id) FROM status_updates 
                               WHERE is_loaded = FALSE AND DATE(reported_at) = CURRENT_DATE),
        'drivers_pending', (SELECT COUNT(*) FROM drivers 
                           WHERE status = 'ACTIVE' 
                           AND driver_id NOT IN (SELECT driver_id FROM status_updates WHERE DATE(reported_at) = CURRENT_DATE)),
        'total_calls_today', (SELECT COUNT(*) FROM call_logs WHERE DATE(created_at) = CURRENT_DATE),
        'completed_calls_today', (SELECT COUNT(*) FROM call_logs 
                                  WHERE call_status = 'COMPLETED' AND DATE(created_at) = CURRENT_DATE),
        'average_call_duration', (SELECT ROUND(AVG(call_duration_seconds)) FROM call_logs 
                                  WHERE call_status = 'COMPLETED' AND DATE(created_at) = CURRENT_DATE),
        'delays_today', (SELECT COUNT(*) FROM status_updates 
                        WHERE is_loaded = FALSE AND DATE(reported_at) = CURRENT_DATE),
        'total_loads_active', (SELECT COUNT(*) FROM loads 
                               WHERE load_status IN ('ASSIGNED', 'LOADING', 'LOADED', 'IN_TRANSIT'))
    ) INTO result;
    
    RETURN result;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION get_dashboard_stats() IS 'Returns JSON with key dashboard statistics';


-- Function: Update Delay Analytics
CREATE OR REPLACE FUNCTION update_delay_analytics()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.is_loaded = FALSE AND NEW.delay_reason_category IS NOT NULL THEN
        -- Check if analytics record exists
        IF EXISTS (
            SELECT 1 FROM delay_analytics 
            WHERE delay_category = NEW.delay_reason_category 
            AND location = NEW.driver_location
        ) THEN
            -- Update existing record
            UPDATE delay_analytics
            SET frequency_count = frequency_count + 1,
                total_delay_minutes = total_delay_minutes + COALESCE(NEW.waiting_duration_minutes, 0),
                average_delay_minutes = (total_delay_minutes + COALESCE(NEW.waiting_duration_minutes, 0)) / (frequency_count + 1),
                last_occurrence = NEW.reported_at,
                estimated_cost_impact = ((total_delay_minutes + COALESCE(NEW.waiting_duration_minutes, 0)) / (frequency_count + 1)),
                updated_at = NOW()
            WHERE delay_category = NEW.delay_reason_category 
            AND location = NEW.driver_location;
        ELSE
            -- Create new record
            INSERT INTO delay_analytics (
                delay_category, location, warehouse_name, frequency_count,
                average_delay_minutes, total_delay_minutes, day_of_week, hour_of_day,
                estimated_cost_impact, first_occurrence, last_occurrence
            ) VALUES (
                NEW.delay_reason_category,
                NEW.driver_location,
                NEW.driver_location,
                1,
                COALESCE(NEW.waiting_duration_minutes, 0),
                COALESCE(NEW.waiting_duration_minutes, 0),
                EXTRACT(DOW FROM NEW.reported_at),
                EXTRACT(HOUR FROM NEW.reported_at),
                COALESCE(NEW.waiting_duration_minutes, 0),
                NEW.reported_at,
                NEW.reported_at
            );
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for automatic delay analytics updates
CREATE TRIGGER trigger_update_delay_analytics
    AFTER INSERT ON status_updates
    FOR EACH ROW
    EXECUTE FUNCTION update_delay_analytics();