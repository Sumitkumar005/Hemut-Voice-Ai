CREATE TABLE IF NOT EXISTS call_logs (
    call_id SERIAL PRIMARY KEY,
    driver_id INTEGER REFERENCES drivers(driver_id) ON DELETE CASCADE,
    
    -- Call Details
    call_sid VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    call_direction VARCHAR(10) DEFAULT 'OUTBOUND' CHECK (call_direction IN ('OUTBOUND', 'INBOUND')),
    call_status VARCHAR(20) DEFAULT 'INITIATED' CHECK (
        call_status IN ('INITIATED', 'RINGING', 'ANSWERED', 'COMPLETED', 'FAILED', 'BUSY', 'NO_ANSWER')
    ),
    
    -- Timing
    call_initiated_at TIMESTAMP WITH TIME ZONE,
    call_answered_at TIMESTAMP WITH TIME ZONE,
    call_ended_at TIMESTAMP WITH TIME ZONE,
    call_duration_seconds INTEGER,
    
    -- Content
    call_transcript TEXT,
    call_summary TEXT,
    call_recording_url TEXT,
    
    -- AI Performance
    ai_confidence_score DECIMAL(3,2) CHECK (ai_confidence_score >= 0 AND ai_confidence_score <= 1),
    sentiment VARCHAR(20) CHECK (sentiment IN ('POSITIVE', 'NEUTRAL', 'NEGATIVE')),
    
    -- Metadata
    vapi_assistant_id VARCHAR(100),
    error_message TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_call_logs_driver ON call_logs(driver_id);
CREATE INDEX idx_call_logs_status ON call_logs(call_status);
CREATE INDEX idx_call_logs_created ON call_logs(created_at);
CREATE INDEX idx_call_logs_sid ON call_logs(call_sid);

COMMENT ON TABLE call_logs IS 'Stores all call history and transcripts';