-- ============================================================================
-- MIGRATION 014: CREATE VIEWS FOR DASHBOARD
-- ============================================================================

-- View: Current Driver Status Summary
CREATE OR REPLACE VIEW vw_driver_status_summary AS
SELECT 
    d.driver_id,
    d.driver_name,
    d.phone_number,
    d.status AS driver_status,
    t.truck_number,
    t.truck_type,
    l.load_id,
    l.load_status,
    l.destination,
    su.is_loaded,
    su.status_type AS latest_status,
    su.reported_at AS last_update,
    CASE 
        WHEN su.is_loaded = TRUE THEN 'LOADED'
        WHEN su.is_loaded = FALSE THEN 'NOT_LOADED'
        ELSE 'PENDING'
    END AS current_load_status
FROM drivers d
LEFT JOIN trucks t ON d.current_truck_id = t.truck_id
LEFT JOIN loads l ON d.driver_id = l.driver_id AND l.load_status IN ('ASSIGNED', 'LOADING', 'LOADED', 'IN_TRANSIT')
LEFT JOIN LATERAL (
    SELECT * FROM status_updates 
    WHERE driver_id = d.driver_id 
    ORDER BY reported_at DESC 
    LIMIT 1
) su ON TRUE
WHERE d.status = 'ACTIVE'
ORDER BY su.reported_at DESC NULLS LAST;

COMMENT ON VIEW vw_driver_status_summary IS 'Real-time summary of all active drivers and their current status';


-- View: Today's Delay Statistics
CREATE OR REPLACE VIEW vw_today_delay_stats AS
SELECT 
    delay_reason_category,
    COUNT(*) AS delay_count,
    AVG(waiting_duration_minutes) AS avg_wait_minutes,
    SUM(waiting_duration_minutes) AS total_wait_minutes,
    COUNT(*) FILTER (WHERE is_recurring_issue = TRUE) AS recurring_issues
FROM status_updates
WHERE is_loaded = FALSE 
    AND DATE(reported_at) = CURRENT_DATE
GROUP BY delay_reason_category
ORDER BY delay_count DESC;

COMMENT ON VIEW vw_today_delay_stats IS 'Delay statistics for today';


-- View: Recent Call History
CREATE OR REPLACE VIEW vw_recent_calls AS
SELECT 
    cl.call_id,
    cl.call_sid,
    d.driver_name,
    cl.phone_number,
    cl.call_status,
    cl.call_duration_seconds,
    cl.sentiment,
    cl.ai_confidence_score,
    su.is_loaded,
    su.status_type,
    cl.created_at AS call_time
FROM call_logs cl
JOIN drivers d ON cl.driver_id = d.driver_id
LEFT JOIN status_updates su ON cl.call_id = su.call_log_id
ORDER BY cl.created_at DESC
LIMIT 50;

COMMENT ON VIEW vw_recent_calls IS 'Last 50 calls with driver information';