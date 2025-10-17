-- ============================================================================
-- MIGRATION 017: VERIFICATION QUERIES
-- ============================================================================

-- Run these queries to verify everything is set up correctly

-- Check all tables exist
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
    AND table_type = 'BASE TABLE'
ORDER BY table_name;

-- Count records in each table
SELECT 
    'drivers' AS table_name, COUNT(*) AS record_count FROM drivers
UNION ALL
SELECT 'trucks', COUNT(*) FROM trucks
UNION ALL
SELECT 'loads', COUNT(*) FROM loads
UNION ALL
SELECT 'call_logs', COUNT(*) FROM call_logs
UNION ALL
SELECT 'status_updates', COUNT(*) FROM status_updates
UNION ALL
SELECT 'delay_analytics', COUNT(*) FROM delay_analytics;

-- Test dashboard stats function
SELECT get_dashboard_stats();

-- View current driver status
SELECT * FROM vw_driver_status_summary;

-- View today's delays
SELECT * FROM vw_today_delay_stats;

-- View recent calls
SELECT * FROM vw_recent_calls LIMIT 10;