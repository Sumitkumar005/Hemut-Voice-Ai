-- ============================================================================
-- MIGRATION 011: SEED SAMPLE CALL LOGS
-- ============================================================================

-- Call logs for loaded drivers
INSERT INTO call_logs (
    driver_id, call_sid, phone_number, call_direction, call_status,
    call_initiated_at, call_answered_at, call_ended_at, call_duration_seconds,
    call_transcript, call_summary, ai_confidence_score, sentiment
) VALUES
(1, 'CALL-' || gen_random_uuid(), '+15551234567', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '30 minutes', NOW() - INTERVAL '30 minutes', NOW() - INTERVAL '27 minutes', 180,
 'AI: Hi John, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: Yes, I am loaded.
AI: Great! Can you tell me what cargo you are hauling?
Driver: Electronics, laptops and monitors.
AI: What is the total weight?
Driver: About 35,000 pounds.
AI: What is your destination?
Driver: Best Buy Distribution Center in Dallas.
AI: When did you finish loading?
Driver: About 30 minutes ago.
AI: Perfect! Any issues to report?
Driver: No, all good.
AI: Thank you John! Have a safe trip.',
 'Driver confirmed loaded with electronics cargo, 35,000 lbs, heading to Dallas. No issues reported.',
 0.95, 'POSITIVE'),

(2, 'CALL-' || gen_random_uuid(), '+15551234568', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '45 minutes', NOW() - INTERVAL '45 minutes', NOW() - INTERVAL '42 minutes', 195,
 'AI: Hi Sarah, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: Yes, just finished loading.
AI: Excellent! What type of cargo?
Driver: Fresh produce - vegetables and fruits.
AI: Total weight?
Driver: 30,000 pounds, about 15 tons.
AI: Where are you headed?
Driver: Whole Foods Market in San Francisco.
AI: When will you depart?
Driver: Leaving in about 10 minutes.
AI: Any concerns?
Driver: No, refrigeration is working perfectly.
AI: Great! Safe travels Sarah.',
 'Driver loaded with refrigerated produce, 30,000 lbs, departing for San Francisco in 10 minutes.',
 0.92, 'POSITIVE'),

(3, 'CALL-' || gen_random_uuid(), '+15551234569', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '1 hour', NOW() - INTERVAL '1 hour', NOW() - INTERVAL '57 minutes', 210,
 'AI: Hi Mike, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: Yeah, I am good to go.
AI: What cargo are you carrying?
Driver: Steel beams and metal sheets, construction materials.
AI: How much weight?
Driver: 50,000 pounds, 25 tons.
AI: Destination?
Driver: Construction site in New York City.
AI: When did loading complete?
Driver: About an hour ago.
AI: Any issues?
Driver: Nope, load is secured properly.
AI: Perfect! Drive safe Mike.',
 'Driver loaded with construction materials, 50,000 lbs, secured and ready for NYC delivery.',
 0.88, 'NEUTRAL');


-- Call logs for NOT loaded drivers (with delays)
INSERT INTO call_logs (
    driver_id, call_sid, phone_number, call_direction, call_status,
    call_initiated_at, call_answered_at, call_ended_at, call_duration_seconds,
    call_transcript, call_summary, ai_confidence_score, sentiment
) VALUES
(4, 'CALL-' || gen_random_uuid(), '+15551234570', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '20 minutes', NOW() - INTERVAL '20 minutes', NOW() - INTERVAL '16 minutes', 240,
 'AI: Hi Emily, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: No, not yet. Still waiting.
AI: Can you tell me why you are not loaded yet?
Driver: There is a long line at the warehouse. About 7 trucks ahead of me.
AI: How long have you been waiting?
Driver: Almost 2 hours now.
AI: What is your estimated loading time?
Driver: They said maybe another hour and a half.
AI: Has this warehouse caused delays before?
Driver: Yes, this is the third time this month. Always backed up.
AI: I understand. Anything urgent we should know?
Driver: No, just frustrating. Losing time.
AI: I have logged this. Our dispatcher will be notified. Thank you Emily.',
 'Driver delayed at warehouse - long queue (7 trucks ahead), waiting 2 hours. Recurring issue at this location (3rd time this month).',
 0.91, 'NEGATIVE'),

(6, 'CALL-' || gen_random_uuid(), '+15551234571', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '35 minutes', NOW() - INTERVAL '35 minutes', NOW() - INTERVAL '32 minutes', 195,
 'AI: Hi David, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: Not loaded yet.
AI: What is causing the delay?
Driver: Mechanical issue with the truck. Brake light is out.
AI: How long will the repair take?
Driver: Mechanic said about 30 minutes. He is working on it now.
AI: Where are you currently?
Driver: At the repair shop near the pickup location.
AI: Is this a recurring problem with this truck?
Driver: No, first time issue.
AI: Okay, I have logged this. Stay safe.
Driver: Thanks, will update once fixed.
AI: Perfect, thank you David.',
 'Driver delayed due to mechanical issue (brake light). Repair in progress, estimated 30 minutes. Not a recurring issue.',
 0.89, 'NEUTRAL'),

(7, 'CALL-' || gen_random_uuid(), '+15551234572', 'OUTBOUND', 'COMPLETED',
 NOW() - INTERVAL '50 minutes', NOW() - INTERVAL '50 minutes', NOW() - INTERVAL '47 minutes', 180,
 'AI: Hi Lisa, this is Hemut AI assistant. Are you loaded and ready to depart?
Driver: No, still at the warehouse.
AI: What is the reason for the delay?
Driver: They cannot find the paperwork. Bill of lading is missing.
AI: How long have you been waiting?
Driver: About 45 minutes.
AI: When do you expect to be loaded?
Driver: Office staff said 20 more minutes once they locate the documents.
AI: Is this location usually an issue?
Driver: Not really, first time problem here.
AI: Understood. I will note this for our records.
Driver: Okay, thanks.
AI: Thank you Lisa.',
 'Driver delayed due to missing paperwork (bill of lading). Waiting 45 minutes, expected resolution in 20 minutes.',
 0.87, 'NEUTRAL');