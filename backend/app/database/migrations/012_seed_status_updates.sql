-- ============================================================================
-- MIGRATION 012: SEED SAMPLE STATUS UPDATES
-- ============================================================================

-- Status updates for LOADED drivers
INSERT INTO status_updates (
    call_log_id, driver_id, truck_id, load_id,
    is_loaded, status_type, cargo_loaded_time, departure_time,
    driver_location, additional_notes, reported_at
) VALUES
-- John Smith - Loaded
((SELECT call_id FROM call_logs WHERE driver_id = 1 ORDER BY created_at DESC LIMIT 1),
 1, 1, 1, TRUE, 'LOADED',
 NOW() - INTERVAL '30 minutes', NOW() + INTERVAL '5 minutes',
 'Amazon Warehouse, Chicago, IL',
 'Driver confirmed all electronics properly secured. Ready to depart.',
 NOW() - INTERVAL '27 minutes'),

-- Sarah Johnson - Loaded
((SELECT call_id FROM call_logs WHERE driver_id = 2 ORDER BY created_at DESC LIMIT 1),
 2, 2, 2, TRUE, 'LOADED',
 NOW() - INTERVAL '45 minutes', NOW() + INTERVAL '10 minutes',
 'Farm Fresh Foods, Salinas, CA',
 'Refrigeration unit operating at correct temperature. Produce loaded carefully.',
 NOW() - INTERVAL '42 minutes'),

-- Mike Davis - Loaded
((SELECT call_id FROM call_logs WHERE driver_id = 3 ORDER BY created_at DESC LIMIT 1),
 3, 3, 3, TRUE, 'LOADED',
 NOW() - INTERVAL '1 hour', NOW() + INTERVAL '15 minutes',
 'Steel Mill, Pittsburgh, PA',
 'Heavy load properly distributed and secured with chains.',
 NOW() - INTERVAL '57 minutes');


-- Status updates for NOT LOADED drivers
INSERT INTO status_updates (
    call_log_id, driver_id, truck_id, load_id,
    is_loaded, status_type, delay_reason_category, delay_reason_details,
    estimated_load_time, waiting_duration_minutes, trucks_in_queue,
    is_recurring_issue, driver_location, additional_notes, reported_at
) VALUES
-- Emily Brown - Warehouse Delay
((SELECT call_id FROM call_logs WHERE driver_id = 4 ORDER BY created_at DESC LIMIT 1),
 4, 4, 5, FALSE, 'DELAYED', 'WAREHOUSE_DELAY',
 'Long queue at warehouse dock. 7 trucks ahead in line.',
 NOW() + INTERVAL '90 minutes', 120, 7, TRUE,
 'Auto Parts Depot, Detroit, MI',
 'This warehouse consistently has delays during peak hours. Third incident this month.',
 NOW() - INTERVAL '16 minutes'),

-- David Wilson - Mechanical Issue
((SELECT call_id FROM call_logs WHERE driver_id = 6 ORDER BY created_at DESC LIMIT 1),
 6, 6, 6, FALSE, 'DELAYED', 'MECHANICAL_ISSUE',
 'Brake light malfunction. Mechanic repairing currently.',
 NOW() + INTERVAL '30 minutes', 45, NULL, FALSE,
 'Repair Shop near Furniture Factory, Grand Rapids, MI',
 'Minor electrical issue. Mechanic on site working on repair. Should be fixed soon.',
 NOW() - INTERVAL '32 minutes'),

-- Lisa Anderson - Paperwork Delay
((SELECT call_id FROM call_logs WHERE driver_id = 7 ORDER BY created_at DESC LIMIT 1),
 7, 8, 7, FALSE, 'DELAYED', 'PAPERWORK',
 'Bill of lading missing. Office staff searching for documents.',
 NOW() + INTERVAL '20 minutes', 45, NULL, FALSE,
 'Food Processing Plant, Minneapolis, MN',
 'Administrative error. Documents misplaced in office. Staff working to locate.',
 NOW() - INTERVAL '47 minutes');