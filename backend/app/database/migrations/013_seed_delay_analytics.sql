-- ============================================================================
-- MIGRATION 013: SEED DELAY ANALYTICS
-- ============================================================================

INSERT INTO delay_analytics (
    delay_category, location, warehouse_name, frequency_count,
    average_delay_minutes, total_delay_minutes, day_of_week, hour_of_day,
    estimated_cost_impact, first_occurrence, last_occurrence
) VALUES
-- Warehouse delay pattern
('WAREHOUSE_DELAY', 'Detroit, MI', 'Auto Parts Depot', 3, 105, 315,
 EXTRACT(DOW FROM NOW()), EXTRACT(HOUR FROM NOW()),
 315.00, NOW() - INTERVAL '30 days', NOW() - INTERVAL '16 minutes'),

('WAREHOUSE_DELAY', 'Chicago, IL', 'Amazon Warehouse', 5, 75, 375,
 EXTRACT(DOW FROM NOW()), EXTRACT(HOUR FROM NOW()),
 375.00, NOW() - INTERVAL '45 days', NOW() - INTERVAL '5 days'),

('MECHANICAL_ISSUE', 'Various Locations', 'On-Road Repairs', 8, 45, 360,
 NULL, NULL, 360.00,
 NOW() - INTERVAL '60 days', NOW() - INTERVAL '32 minutes'),

('PAPERWORK', 'Various Locations', 'Multiple Warehouses', 12, 35, 420,
 NULL, NULL, 420.00,
 NOW() - INTERVAL '90 days', NOW() - INTERVAL '47 minutes'),

('TRAFFIC', 'Various Highways', 'Interstate Delays', 15, 55, 825,
 NULL, NULL, 825.00,
 NOW() - INTERVAL '60 days', NOW() - INTERVAL '10 days');