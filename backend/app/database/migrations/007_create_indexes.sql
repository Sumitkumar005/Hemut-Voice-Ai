CREATE INDEX idx_loads_driver_status ON loads(driver_id, load_status);
CREATE INDEX idx_loads_truck_status ON loads(truck_id, load_status);
CREATE INDEX idx_status_driver_reported ON status_updates(driver_id, reported_at DESC);
CREATE INDEX idx_call_logs_driver_created ON call_logs(driver_id, created_at DESC);

-- Full-text search indexes (for searching transcripts and notes)
CREATE INDEX idx_call_transcript_search ON call_logs USING gin(to_tsvector('english', call_transcript));
CREATE INDEX idx_status_notes_search ON status_updates USING gin(to_tsvector('english', additional_notes));