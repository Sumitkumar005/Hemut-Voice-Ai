# HEMUT LOAD STATUS VOICE AI AGENT
## Internship Assignment Documentation

---

## 📋 TABLE OF CONTENTS
1. [Company Overview](#company-overview)
2. [Problem Statement - Detailed Analysis](#problem-statement)
3. [Solution Architecture](#solution-architecture)
4. [Technical Requirements](#technical-requirements)
5. [Database Schema Design](#database-schema)
6. [VAPI Voice AI Configuration](#vapi-configuration)
7. [Backend API Endpoints](#backend-api)
8. [Frontend Dashboard Design](#frontend-design)
9. [Implementation Roadmap](#implementation-roadmap)
10. [Testing Strategy](#testing-strategy)

---

## 🏢 COMPANY OVERVIEW

### About Hemut (YC W25)
**Founded:** 2024  
**Location:** Rockford, Illinois  
**Industry:** Transportation Management Software  
**Mission:** Transforming the $875B American trucking industry

### The Problem Hemut is Solving
- **74%** of trucking companies still operate on paper, Excel, and phone calls
- **26%** using software rely on outdated systems from early 2000s
- Legacy systems suffer from crashes, poor integrations, and inefficiency
- Dispatchers spend hours on manual phone calls checking driver status
- Load tracking is fragmented and error-prone
- No real-time visibility into fleet operations

### Hemut's Solution
Building next-generation Transportation Management System (TMS) with specialized AI Agents that automate:
- Dispatching
- Load planning
- Billing
- Compliance
- **Driver Status Tracking** ← YOUR PROJECT

---

## 🎯 PROBLEM STATEMENT - DETAILED ANALYSIS

### Current Industry Pain Points

#### 1. **Manual Driver Check-Ins**
**Current Process:**
- Dispatchers call 20-50 drivers daily (sometimes multiple times)
- Each call takes 2-5 minutes
- Drivers miss calls while driving (safety regulations)
- Information gets lost in handwritten notes
- No centralized tracking system

**Real-World Scenario:**
```
8:00 AM - Dispatcher calls Driver John
         "Are you loaded?"
         Driver: "No, still waiting at warehouse"
         Dispatcher: "Why?"
         Driver: "Paperwork delay"
         
9:30 AM - Dispatcher calls again
         "Are you loaded now?"
         Driver: "Yes, loaded 30 minutes ago"
         
Result: 90 minutes lost, information recorded manually
```

#### 2. **Load Status Information Gap**
Dispatchers need to know:
- ✅ Is the truck loaded?
- ✅ When was it loaded?
- ✅ What cargo? (Type, weight, quantity)
- ✅ If NOT loaded, WHY? (Root cause analysis)
- ✅ Current location
- ✅ Estimated departure time
- ✅ Any issues or delays

**Current Problems:**
- Information scattered across phone notes, texts, and memory
- No historical data for analysis
- Can't identify recurring delay patterns
- No visibility for customers
- Manual reporting takes hours

#### 3. **Operational Inefficiencies**

**Time Wastage:**
- Dispatcher makes 40 calls/day × 3 minutes = 2 hours on phone
- Cost: $20/hour × 2 hours = $40/day = $10,400/year per dispatcher
- For 10 dispatchers = **$104,000/year wasted**

**Missed Revenue:**
- Delayed load info = Can't assign next load quickly
- Empty miles increase
- Driver utilization drops
- Customer satisfaction suffers

---

## 💡 YOUR ASSIGNMENT: AI-POWERED SOLUTION

### What You're Building

**"Load Status Voice AI Agent"** - An outbound calling system that:

1. **Automatically calls drivers** at scheduled times
2. **Asks intelligent questions** about load status
3. **Records structured data** in database
4. **Provides real-time dashboard** for dispatchers
5. **Identifies delay patterns** through analytics

### Conversation Flow Design

#### **FLOW 1: Driver is LOADED ✅**
```
AI: "Hi John, this is Hemut AI assistant. Are you loaded and ready to go?"

Driver: "Yes, I'm loaded"

AI: "Great! Can you tell me what cargo you're hauling?"

Driver: "20 pallets of electronics"

AI: "What's the total weight?"

Driver: "35,000 pounds"

AI: "What's your destination?"

Driver: "Dallas warehouse on 5th Street"

AI: "When did you complete loading?"

Driver: "About 30 minutes ago, around 9:30 AM"

AI: "Perfect! What time are you departing?"

Driver: "Leaving in 15 minutes"

AI: "Excellent! Any issues or concerns I should log?"

Driver: "No, all good"

AI: "Thank you John! Have a safe trip. This information has been recorded."

✅ Data Stored:
- Status: LOADED
- Cargo Type: Electronics
- Cargo Quantity: 20 pallets
- Weight: 35,000 lbs
- Destination: Dallas warehouse, 5th Street
- Load Completed Time: 9:30 AM
- Departure Time: 9:45 AM
- Issues: None
```

#### **FLOW 2: Driver is NOT LOADED ❌**
```
AI: "Hi Sarah, this is Hemut AI assistant. Are you loaded and ready to go?"

Driver: "No, not yet"

AI: "I understand. Can you tell me why you're not loaded yet?"

Driver: "The warehouse is backed up, long queue"

AI: "I see. How many trucks are ahead of you?"

Driver: "About 5 trucks"

AI: "What's your estimated loading time?"

Driver: "They said maybe 2 more hours"

AI: "Has this warehouse caused delays before?"

Driver: "Yeah, this is the third time this month"

AI: "I've noted that. Is there anything urgent we should know?"

Driver: "No, just the delay"

AI: "Thanks Sarah. I'll log this and our dispatcher will be notified. Stay safe!"

❌ Data Stored:
- Status: NOT LOADED
- Reason Category: Warehouse Delay
- Detailed Reason: Warehouse backed up, 5 trucks ahead
- Estimated Load Time: 2 hours
- Recurring Issue: Yes (3rd time this month)
- Location: [Auto-captured from GPS]
- Time Reported: 10:15 AM
```

---

## 🏗️ SOLUTION ARCHITECTURE

### System Components

```
┌─────────────────────────────────────────────────┐
│           FRONTEND (React + Vite)               │
│  - Dispatcher Dashboard                         │
│  - Real-time Load Status Board                  │
│  - Driver Management                            │
│  - Analytics & Reports                          │
└──────────────────┬──────────────────────────────┘
                   │ REST API
                   ↓
┌─────────────────────────────────────────────────┐
│         BACKEND (FastAPI + Python)              │
│  - Webhook Handlers                             │
│  - Business Logic                               │
│  - Database Operations                          │
│  - VAPI Integration                             │
└──────────────────┬──────────────────────────────┘
                   │
         ┌─────────┴─────────┐
         ↓                   ↓
┌──────────────────┐  ┌─────────────────┐
│   PostgreSQL     │  │    VAPI.AI      │
│   Database       │  │  Voice Agent    │
│                  │  │                 │
│  - drivers       │  │  - Outbound     │
│  - trucks        │  │    Calls        │
│  - loads         │  │  - Speech-to-   │
│  - call_logs     │  │    Text         │
│  - status_       │  │  - AI Response  │
│    updates       │  │  - Webhooks     │
└──────────────────┘  └─────────────────┘
```

---

## 🗄️ DATABASE SCHEMA DESIGN

### Tables Structure

#### **1. drivers**
```sql
CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    driver_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    license_number VARCHAR(50) UNIQUE,
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'ACTIVE',  -- ACTIVE, INACTIVE, ON_LEAVE
    current_truck_id INTEGER,
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **2. trucks**
```sql
CREATE TABLE trucks (
    truck_id SERIAL PRIMARY KEY,
    truck_number VARCHAR(50) UNIQUE NOT NULL,
    truck_type VARCHAR(50),  -- FLATBED, REFRIGERATED, DRY_VAN, TANKER
    capacity_lbs INTEGER,
    vin_number VARCHAR(50) UNIQUE,
    license_plate VARCHAR(20),
    current_location TEXT,
    status VARCHAR(20) DEFAULT 'AVAILABLE',  -- AVAILABLE, IN_TRANSIT, MAINTENANCE
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **3. loads**
```sql
CREATE TABLE loads (
    load_id SERIAL PRIMARY KEY,
    driver_id INTEGER REFERENCES drivers(driver_id),
    truck_id INTEGER REFERENCES trucks(truck_id),
    
    -- Load Details
    cargo_type VARCHAR(100),
    cargo_description TEXT,
    cargo_quantity VARCHAR(50),  -- "20 pallets", "15 tons", etc.
    weight_lbs DECIMAL(10,2),
    
    -- Location & Time
    pickup_location TEXT,
    destination TEXT,
    load_completed_time TIMESTAMP,
    scheduled_departure_time TIMESTAMP,
    actual_departure_time TIMESTAMP,
    estimated_arrival_time TIMESTAMP,
    actual_arrival_time TIMESTAMP,
    
    -- Status
    load_status VARCHAR(30) DEFAULT 'ASSIGNED',  
    -- ASSIGNED, LOADING, LOADED, IN_TRANSIT, DELIVERED, CANCELLED
    
    -- Additional Info
    special_instructions TEXT,
    temperature_control BOOLEAN DEFAULT FALSE,
    hazmat BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **4. status_updates**
```sql
CREATE TABLE status_updates (
    update_id SERIAL PRIMARY KEY,
    call_log_id INTEGER REFERENCES call_logs(call_id),
    driver_id INTEGER REFERENCES drivers(driver_id),
    truck_id INTEGER REFERENCES trucks(truck_id),
    load_id INTEGER REFERENCES loads(load_id),
    
    -- Status Info
    is_loaded BOOLEAN NOT NULL,
    status_type VARCHAR(30),  -- LOADED, NOT_LOADED, DELAYED, ISSUE
    
    -- If NOT LOADED
    delay_reason_category VARCHAR(50),  
    -- WAREHOUSE_DELAY, MECHANICAL_ISSUE, WEATHER, PAPERWORK, 
    -- TRAFFIC, LOADING_EQUIPMENT, OTHER
    
    delay_reason_details TEXT,
    estimated_load_time TIMESTAMP,
    trucks_in_queue INTEGER,
    is_recurring_issue BOOLEAN DEFAULT FALSE,
    
    -- If LOADED
    cargo_loaded_time TIMESTAMP,
    departure_time TIMESTAMP,
    
    -- Common Fields
    driver_location TEXT,
    additional_notes TEXT,
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **5. call_logs**
```sql
CREATE TABLE call_logs (
    call_id SERIAL PRIMARY KEY,
    driver_id INTEGER REFERENCES drivers(driver_id),
    
    -- Call Details
    call_sid VARCHAR(100),  -- VAPI Call ID
    phone_number VARCHAR(20),
    call_direction VARCHAR(10),  -- OUTBOUND, INBOUND
    call_status VARCHAR(20),  -- INITIATED, RINGING, ANSWERED, COMPLETED, FAILED, BUSY, NO_ANSWER
    
    -- Timing
    call_initiated_at TIMESTAMP,
    call_answered_at TIMESTAMP,
    call_ended_at TIMESTAMP,
    call_duration_seconds INTEGER,
    
    -- Content
    call_transcript TEXT,
    call_summary TEXT,
    call_recording_url TEXT,
    
    -- AI Performance
    ai_confidence_score DECIMAL(3,2),  -- 0.00 to 1.00
    sentiment VARCHAR(20),  -- POSITIVE, NEUTRAL, NEGATIVE
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **6. delay_analytics**
```sql
CREATE TABLE delay_analytics (
    analytics_id SERIAL PRIMARY KEY,
    
    -- Pattern Analysis
    delay_category VARCHAR(50),
    location VARCHAR(200),
    warehouse_name VARCHAR(100),
    frequency_count INTEGER DEFAULT 1,
    average_delay_minutes INTEGER,
    
    -- Time Patterns
    day_of_week INTEGER,  -- 1-7 (Monday-Sunday)
    time_of_day TIME,
    
    -- Cost Impact
    estimated_cost_impact DECIMAL(10,2),
    
    first_occurrence TIMESTAMP,
    last_occurrence TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎤 VAPI VOICE AI CONFIGURATION

### VAPI Setup Steps

#### **Step 1: Create VAPI Account**
1. Go to https://vapi.ai
2. Sign up for account
3. Add $5 credit (goes a long way for testing)
4. Navigate to Dashboard

#### **Step 2: Create Assistant**

**Basic Settings:**
- **Name:** Hemut Load Status Agent
- **Type:** Outbound Calling
- **Language:** English (US)
- **Voice Provider:** ElevenLabs or OpenAI
- **Voice Selection:** Professional, clear male/female voice

#### **Step 3: System Prompt**

```markdown
ROLE:
You are an AI assistant for Hemut, a trucking management company. Your job is to call truck drivers and collect load status information.

PERSONALITY:
- Professional but friendly
- Clear and concise
- Patient and understanding
- Empathetic to driver challenges

CONVERSATION FLOW:

1. GREETING:
   "Hi [Driver Name], this is the Hemut AI assistant. I'm calling to check on your load status. Do you have a moment?"
   
2. MAIN QUESTION:
   "Are you loaded and ready to depart?"
   
3A. IF YES (LOADED):
   - Ask: "What cargo are you hauling?"
   - Ask: "What's the total weight in pounds?"
   - Ask: "What quantity? (pallets, tons, etc.)"
   - Ask: "What's your destination?"
   - Ask: "When did you finish loading?"
   - Ask: "What time are you departing?"
   - Ask: "Any issues or concerns?"
   
3B. IF NO (NOT LOADED):
   - Ask: "Can you tell me why you're not loaded yet?"
   - Ask: "What's causing the delay?"
   - Ask: "How long have you been waiting?"
   - Ask: "What's your estimated loading time?"
   - Ask: "Is this location/warehouse a recurring issue?"
   - Ask: "Anything urgent we should know?"

4. CLOSING:
   "Thank you [Driver Name]! This information has been recorded. Stay safe out there!"

RULES:
- Keep conversation under 3 minutes
- Be respectful of driver's time
- If driver is busy, ask when to call back
- If driver sounds stressed, be extra empathetic
- Confirm all numbers and details before ending
- Never argue or debate with driver
- If information is unclear, politely ask for clarification

DATA COLLECTION:
Extract and structure the following information:
- Load Status (boolean: loaded/not loaded)
- Cargo Type (string)
- Weight (number in pounds)
- Quantity (string)
- Destination (string)
- Load Time (timestamp)
- Departure Time (timestamp)
- Delay Reason (if not loaded)
- Additional Notes (string)
```

#### **Step 4: Configure Tools/Functions**

**Function 1: record_loaded_status**
```json
{
  "name": "record_loaded_status",
  "description": "Records when a driver is loaded and ready to depart",
  "parameters": {
    "type": "object",
    "properties": {
      "driver_id": {
        "type": "integer",
        "description": "Driver's unique ID"
      },
      "is_loaded": {
        "type": "boolean",
        "description": "True if loaded, False if not"
      },
      "cargo_type": {
        "type": "string",
        "description": "Type of cargo (electronics, food, machinery, etc.)"
      },
      "weight_lbs": {
        "type": "number",
        "description": "Total weight in pounds"
      },
      "cargo_quantity": {
        "type": "string",
        "description": "Quantity description (20 pallets, 15 tons, etc.)"
      },
      "destination": {
        "type": "string",
        "description": "Delivery destination address"
      },
      "load_completed_time": {
        "type": "string",
        "format": "date-time",
        "description": "ISO 8601 timestamp when loading completed"
      },
      "departure_time": {
        "type": "string",
        "format": "date-time",
        "description": "ISO 8601 timestamp when departing"
      },
      "issues_notes": {
        "type": "string",
        "description": "Any issues or additional notes"
      }
    },
    "required": ["driver_id", "is_loaded"]
  }
}
```

**Function 2: record_not_loaded_status**
```json
{
  "name": "record_not_loaded_status",
  "description": "Records when a driver is NOT loaded and reasons for delay",
  "parameters": {
    "type": "object",
    "properties": {
      "driver_id": {
        "type": "integer",
        "description": "Driver's unique ID"
      },
      "is_loaded": {
        "type": "boolean",
        "description": "False - driver is not loaded"
      },
      "delay_reason_category": {
        "type": "string",
        "enum": [
          "WAREHOUSE_DELAY",
          "MECHANICAL_ISSUE",
          "WEATHER",
          "PAPERWORK",
          "TRAFFIC",
          "LOADING_EQUIPMENT",
          "OTHER"
        ],
        "description": "Category of delay"
      },
      "delay_reason_details": {
        "type": "string",
        "description": "Detailed explanation of the delay"
      },
      "estimated_load_time": {
        "type": "string",
        "format": "date-time",
        "description": "Estimated time when loading will complete"
      },
      "waiting_duration_minutes": {
        "type": "integer",
        "description": "How long driver has been waiting"
      },
      "trucks_in_queue": {
        "type": "integer",
        "description": "Number of trucks ahead in queue"
      },
      "is_recurring_issue": {
        "type": "boolean",
        "description": "Is this a recurring problem at this location?"
      },
      "current_location": {
        "type": "string",
        "description": "Current location/warehouse name"
      }
    },
    "required": ["driver_id", "is_loaded", "delay_reason_details"]
  }
}
```

#### **Step 5: Webhook Configuration**

**Webhook URL:** `https://your-backend-api.com/api/webhooks/vapi`

**Events to Subscribe:**
- `call.started` - When call is initiated
- `call.ended` - When call completes
- `function.called` - When AI calls a function
- `transcript.updated` - Real-time transcript updates

---

## 🔧 BACKEND API ENDPOINTS (FastAPI)

### API Structure

```python
# main.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
import asyncpg
import httpx
import os

app = FastAPI(title="Hemut Load Status API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")
```

### Endpoint Definitions

#### **1. Driver Management**

```python
# GET /api/drivers - Get all drivers
@app.get("/api/drivers")
async def get_drivers(status: Optional[str] = None):
    """
    Retrieve all drivers or filter by status
    Query params: ?status=ACTIVE
    """
    pass

# POST /api/drivers - Create new driver
@app.post("/api/drivers")
async def create_driver(driver: DriverCreate):
    """
    Create a new driver
    Body: {
        "driver_name": "John Smith",
        "phone_number": "+15551234567",
        "license_number": "DL12345",
        "email": "john@email.com"
    }
    """
    pass

# GET /api/drivers/{driver_id} - Get specific driver
@app.get("/api/drivers/{driver_id}")
async def get_driver(driver_id: int):
    pass

# PUT /api/drivers/{driver_id} - Update driver
@app.put("/api/drivers/{driver_id}")
async def update_driver(driver_id: int, driver: DriverUpdate):
    pass
```

#### **2. Load Management**

```python
# GET /api/loads - Get all loads
@app.get("/api/loads")
async def get_loads(
    status: Optional[str] = None,
    driver_id: Optional[int] = None,
    date_from: Optional[datetime] = None,
    date_to: Optional[datetime] = None
):
    """
    Get loads with optional filters
    Query params: 
    ?status=LOADED
    &driver_id=5
    &date_from=2024-10-01
    &date_to=2024-10-17
    """
    pass

# POST /api/loads - Create new load assignment
@app.post("/api/loads")
async def create_load(load: LoadCreate):
    """
    Assign a new load to driver/truck
    Body: {
        "driver_id": 5,
        "truck_id": 3,
        "pickup_location": "Warehouse A, Chicago",
        "destination": "Distribution Center, Dallas",
        "scheduled_departure_time": "2024-10-17T14:00:00Z"
    }
    """
    pass

# GET /api/loads/{load_id} - Get specific load
@app.get("/api/loads/{load_id}")
async def get_load(load_id: int):
    pass

# PUT /api/loads/{load_id}/status - Update load status
@app.put("/api/loads/{load_id}/status")
async def update_load_status(load_id: int, status: LoadStatusUpdate):
    pass
```

#### **3. VAPI Integration**

```python
# POST /api/vapi/initiate-call - Trigger outbound call
@app.post("/api/vapi/initiate-call")
async def initiate_vapi_call(call_request: CallRequest):
    """
    Initiate outbound call to driver via VAPI
    Body: {
        "driver_id": 5,
        "phone_number": "+15551234567",
        "priority": "normal"
    }
    """
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {VAPI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "assistant": {
                "assistantId": VAPI_ASSISTANT_ID
            },
            "phoneNumberId": "your-phone-number-id",
            "customer": {
                "number": call_request.phone_number,
                "name": call_request.driver_name
            }
        }
        
        response = await client.post(
            "https://api.vapi.ai/call/phone",
            headers=headers,
            json=payload
        )
        
        return response.json()

# POST /api/vapi/bulk-call - Initiate multiple calls
@app.post("/api/vapi/bulk-call")
async def initiate_bulk_calls(
    driver_ids: List[int],
    background_tasks: BackgroundTasks
):
    """
    Initiate calls to multiple drivers
    Body: {
        "driver_ids": [1, 2, 3, 5, 8]
    }
    """
    for driver_id in driver_ids:
        background_tasks.add_task(call_driver, driver_id)
    
    return {"message": f"Initiated {len(driver_ids)} calls"}
```

#### **4. Webhook Handlers**

```python
# POST /api/webhooks/vapi - VAPI webhook receiver
@app.post("/api/webhooks/vapi")
async def vapi_webhook(webhook_data: dict):
    """
    Receives webhooks from VAPI
    Events:
    - call.started
    - call.ended
    - function.called
    - transcript.updated
    """
    event_type = webhook_data.get("type")
    
    if event_type == "function.called":
        function_name = webhook_data.get("function").get("name")
        
        if function_name == "record_loaded_status":
            await handle_loaded_status(webhook_data)
        
        elif function_name == "record_not_loaded_status":
            await handle_not_loaded_status(webhook_data)
    
    elif event_type == "call.ended":
        await handle_call_ended(webhook_data)
    
    return {"status": "received"}

async def handle_loaded_status(data: dict):
    """Process loaded status data"""
    params = data.get("function").get("parameters")
    
    # Store in status_updates table
    query = """
        INSERT INTO status_updates (
            driver_id, is_loaded, cargo_type, weight_lbs,
            cargo_quantity, destination, cargo_loaded_time,
            departure_time, additional_notes, reported_at
        ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, NOW())
        RETURNING update_id
    """
    
    # Execute database insert
    # Update load table
    # Send real-time notification to frontend
    
async def handle_not_loaded_status(data: dict):
    """Process not loaded status data"""
    params = data.get("function").get("parameters")
    
    # Store in status_updates table
    # Check for recurring issues
    # Update delay_analytics
    # Alert dispatcher if critical
```

#### **5. Analytics & Reports**

```python
# GET /api/analytics/dashboard - Dashboard statistics
@app.get("/api/analytics/dashboard")
async def get_dashboard_stats():
    """
    Returns:
    {
        "total_drivers": 50,
        "drivers_loaded": 35,
        "drivers_not_loaded": 10,
        "drivers_pending": 5,
        "average_load_time_minutes": 45,
        "delays_today": 8,
        "top_delay_reasons": [...]
    }
    """
    pass

# GET /api/analytics/delays - Delay pattern analysis
@app.get("/api/analytics/delays")
async def get_delay_analytics(
    days: int = 30,
    group_by: str = "reason"
):
    """
    Analyze delay patterns
    Query params: ?days=30&group_by=reason
    group_by options: reason, location, time_of_day, day_of_week
    """
    pass

# GET /api/analytics/driver-performance - Driver metrics
@app.get("/api/analytics/driver-performance/{driver_id}")
async def get_driver_performance(driver_id: int, days: int = 30):
    """
    Driver performance metrics:
    - Average load time
    - Delay frequency
    - On-time percentage
    - Total loads completed
    """
    pass
```

#### **6. Call Logs**

```python
# GET /api/call-logs - Get call history
@app.get("/api/call-logs")
async def get_call_logs(
    driver_id: Optional[int] = None,
    date_from: Optional[datetime] = None,
    date_to: Optional[datetime] = None,
    status: Optional[str] = None
):
    """
    Retrieve call logs with filters
    """
    pass

# GET /api/call-logs/{call_id} - Get specific call
@app.get("/api/call-logs/{call_id}")
async def get_call_log(call_id: int):
    """
    Get detailed call information including:
    - Full transcript
    - Call duration
    - Status updates made
    - Recording URL
    """
    pass

# GET /api/call-logs/{call_id}/transcript - Get transcript
@app.get("/api/call-logs/{call_id}/transcript")
async def get_call_transcript(call_id: int):
    pass
```

---

## 🎨 FRONTEND DASHBOARD DESIGN (React + Vite)

### Page Structure

#### **1. Dashboard Home**
Real-time overview of fleet status

**Components:**
- **Status Cards**
  - Total Drivers
  - Loaded & Ready (Green)
  - Not Loaded (Red)
  - Pending Calls (Yellow)
  
- **Live Status Board**
  Table showing all drivers with:
  - Driver Name
  - Truck Number
  - Load Status (Badge)
  - Last Update Time
  - Action Buttons (Call Now, View Details)

- **Recent Calls Feed**
  Real-time list of completed calls

- **Delay Alert Panel**
  Highlights drivers with delays

#### **2. Driver Management Page**

**Features:**
- Driver list with search/filter
- Add new driver button
- Edit driver information
- View driver history
- Performance metrics per driver

#### **3. Load Tracking Page**

**Features:**
- Current loads table
- Load details modal
- Status timeline
- Map view (optional)

#### **4. Call History Page**

**Features:**
- Searchable call log table
- Filter by date, driver, status
- Play call recordings
- View transcripts
- Export to CSV

#### **5. Analytics Dashboard**

**Charts & Graphs:**
- Delay trends over time (line chart)
- Delay reasons breakdown (pie chart)
- Busiest times for delays (heatmap)
- Top problematic locations (bar chart)
- Driver performance comparison

---

## 🚀 IMPLEMENTATION ROADMAP

### **Phase 1: Setup & Foundation (Days 1-2)**

**Day 1: Environment Setup**
- ✅ Install Node.js, Python 3.9+, PostgreSQL
- ✅ Create project folder structure
- ✅ Initialize Git repository
- ✅ Set up virtual environment for Python
- ✅ Create React + Vite project
- ✅ Install dependencies:
  ```bash
  # Backend
  pip install fastapi uvicorn sqlalchemy asyncpg python-dotenv httpx pydantic
  
  # Frontend
  npm create vite@latest hemut-frontend -- --template react
  cd hemut-frontend
  npm install axios react-router-dom @tanstack/react-query lucide-react
  npm install -D tailwindcss postcss autoprefixer
  ```
- ✅ Create `.env` file for environment variables
- ✅ Set up PostgreSQL database

**Day 2: Database Setup**
- ✅ Write SQL schema (all tables)
- ✅ Create database migration scripts
- ✅ Seed dummy data:
  - 10 sample drivers
  - 10 sample trucks
  - 5 sample loads
- ✅ Test database connections
- ✅ Write database helper functions

---

### **Phase 2: VAPI Configuration (Days 3-4)**

**Day 3: VAPI Account Setup**
- ✅ Create VAPI account at https://vapi.ai
- ✅ Add payment method ($5 credit)
- ✅ Get API keys (save to `.env`)
- ✅ Purchase a phone number (for outbound calls)
- ✅ Test VAPI dashboard

**Day 4: AI Assistant Configuration**
- ✅ Create new Assistant in VAPI dashboard
- ✅ Configure system prompt (copy from this document)
- ✅ Set up voice settings (ElevenLabs or OpenAI)
- ✅ Configure two functions:
  - `record_loaded_status`
  - `record_not_loaded_status`
- ✅ Set up webhook URL (use ngrok for local testing)
- ✅ Test assistant with manual call

---

### **Phase 3: Backend Development (Days 5-8)**

**Day 5: Core API Setup**
- ✅ Create FastAPI app structure
- ✅ Set up CORS middleware
- ✅ Create database connection pool
- ✅ Write Pydantic models for request/response
- ✅ Implement health check endpoint
- ✅ Test with Postman/Thunder Client

**Day 6: Driver & Load Endpoints**
- ✅ Implement driver CRUD operations:
  - GET /api/drivers
  - POST /api/drivers
  - GET /api/drivers/{id}
  - PUT /api/drivers/{id}
  - DELETE /api/drivers/{id}
- ✅ Implement load endpoints:
  - GET /api/loads
  - POST /api/loads
  - GET /api/loads/{id}
  - PUT /api/loads/{id}/status
- ✅ Write unit tests

**Day 7: VAPI Integration**
- ✅ Implement outbound call endpoint:
  - POST /api/vapi/initiate-call
- ✅ Implement bulk call endpoint:
  - POST /api/vapi/bulk-call
- ✅ Implement webhook receiver:
  - POST /api/webhooks/vapi
- ✅ Handle function calls from VAPI:
  - `handle_loaded_status()`
  - `handle_not_loaded_status()`
- ✅ Store call logs in database
- ✅ Test end-to-end call flow

**Day 8: Analytics & Call Logs**
- ✅ Implement analytics endpoints:
  - GET /api/analytics/dashboard
  - GET /api/analytics/delays
  - GET /api/analytics/driver-performance/{id}
- ✅ Implement call log endpoints:
  - GET /api/call-logs
  - GET /api/call-logs/{id}
  - GET /api/call-logs/{id}/transcript
- ✅ Write SQL queries for aggregations
- ✅ Test all endpoints

---

### **Phase 4: Frontend Development (Days 9-13)**

**Day 9: Project Setup & Routing**
- ✅ Configure Tailwind CSS
- ✅ Set up React Router
- ✅ Create layout components:
  - Navbar
  - Sidebar
  - Footer
- ✅ Set up route structure:
  - / → Dashboard
  - /drivers → Driver Management
  - /loads → Load Tracking
  - /calls → Call History
  - /analytics → Analytics

**Day 10: Dashboard Page**
- ✅ Create status cards component
- ✅ Build live status board:
  - Driver table with real-time updates
  - Status badges (Loaded/Not Loaded/Pending)
  - Action buttons
- ✅ Recent calls feed
- ✅ Delay alert panel
- ✅ Connect to backend APIs
- ✅ Implement auto-refresh (polling or WebSocket)

**Day 11: Driver & Load Management Pages**
- ✅ Driver Management:
  - Driver list table with search/filter
  - Add driver modal/form
  - Edit driver modal
  - Delete confirmation
  - View driver details page
- ✅ Load Tracking:
  - Load list table
  - Load details modal
  - Status timeline component
  - Filter by status/date
- ✅ Form validations
- ✅ Error handling

**Day 12: Call History & Analytics**
- ✅ Call History Page:
  - Call log table with filters
  - Date range picker
  - Call details modal
  - Transcript viewer
  - Audio player (if recordings available)
  - Export to CSV button
- ✅ Analytics Page:
  - Install chart library (recharts or chart.js)
  - Delay trends line chart
  - Delay reasons pie chart
  - Top locations bar chart
  - Driver performance comparison

**Day 13: Real-time Features & Polish**
- ✅ Implement WebSocket or polling for live updates
- ✅ Add notifications/toasts for:
  - New calls completed
  - Delays detected
  - System alerts
- ✅ Loading states & skeletons
- ✅ Error boundaries
- ✅ Responsive design for mobile
- ✅ Dark mode (optional)

---

### **Phase 5: Integration & Testing (Days 14-15)**

**Day 14: End-to-End Testing**
- ✅ Manual testing of complete flow:
  1. Add a driver
  2. Assign a load
  3. Trigger outbound call
  4. Receive webhook
  5. Verify data in database
  6. Check dashboard updates
- ✅ Test both scenarios (Loaded & Not Loaded)
- ✅ Test error cases:
  - Driver doesn't answer
  - Invalid phone number
  - Database errors
  - API failures
- ✅ Performance testing:
  - Load test with 100 simultaneous calls
  - Database query optimization
  - API response times

**Day 15: Bug Fixes & Documentation**
- ✅ Fix all identified bugs
- ✅ Write API documentation (Swagger/OpenAPI)
- ✅ Write README.md with:
  - Project overview
  - Setup instructions
  - Environment variables
  - How to run locally
  - API endpoints
- ✅ Create demo video (optional)
- ✅ Prepare presentation slides

---

### **Phase 6: Deployment & Presentation (Days 16-17)**

**Day 16: Deployment**
- ✅ Deploy backend to:
  - Heroku, Railway, or Render
  - Or AWS EC2/DigitalOcean
- ✅ Deploy database to:
  - Railway PostgreSQL
  - Or AWS RDS
  - Or Supabase
- ✅ Deploy frontend to:
  - Vercel or Netlify
- ✅ Update VAPI webhook URL to production
- ✅ Test production environment
- ✅ Set up monitoring (optional)

**Day 17: Final Review & Presentation**
- ✅ Final testing in production
- ✅ Prepare demo script
- ✅ Create presentation slides covering:
  - Problem statement
  - Solution overview
  - Technical architecture
  - Key features
  - Demo walkthrough
  - Future enhancements
- ✅ Practice presentation
- ✅ Submit assignment

---

## 🧪 TESTING STRATEGY

### **1. Backend Testing**

**Unit Tests (pytest)**
```python
# test_drivers.py
def test_create_driver():
    response = client.post("/api/drivers", json={
        "driver_name": "Test Driver",
        "phone_number": "+15551234567",
        "license_number": "DL12345"
    })
    assert response.status_code == 201
    assert response.json()["driver_name"] == "Test Driver"

def test_get_drivers():
    response = client.get("/api/drivers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# test_vapi.py
def test_initiate_call():
    response = client.post("/api/vapi/initiate-call", json={
        "driver_id": 1,
        "phone_number": "+15551234567"
    })
    assert response.status_code == 200
    assert "call_id" in response.json()

def test_webhook_loaded_status():
    webhook_data = {
        "type": "function.called",
        "function": {
            "name": "record_loaded_status",
            "parameters": {
                "driver_id": 1,
                "is_loaded": True,
                "cargo_type": "Electronics",
                "weight_lbs": 35000
            }
        }
    }
    response = client.post("/api/webhooks/vapi", json=webhook_data)
    assert response.status_code == 200
```

### **2. Frontend Testing**

**Component Tests (React Testing Library)**
```javascript
// DriverList.test.jsx
test('renders driver list', async () => {
  render(<DriverList />);
  expect(await screen.findByText(/Total Drivers/i)).toBeInTheDocument();
});

test('filters drivers by status', async () => {
  render(<DriverList />);
  const filterSelect = screen.getByLabelText(/Status/i);
  fireEvent.change(filterSelect, { target: { value: 'ACTIVE' } });
  // Assert filtered results
});
```

### **3. Integration Testing**

**Test Scenarios:**
1. **Happy Path - Loaded Driver:**
   - Create driver in database
   - Assign load
   - Trigger call
   - Simulate VAPI webhook with loaded status
   - Verify dashboard shows "Loaded"
   - Verify data in database

2. **Happy Path - Not Loaded Driver:**
   - Create driver in database
   - Assign load
   - Trigger call
   - Simulate VAPI webhook with delay reason
   - Verify dashboard shows "Delayed"
   - Verify analytics updated

3. **Error Scenarios:**
   - Call to invalid phone number
   - Driver doesn't answer
   - Database connection failure
   - VAPI API rate limit

### **4. Manual Testing Checklist**

**Dashboard:**
- [ ] Status cards show correct counts
- [ ] Live status board updates in real-time
- [ ] Action buttons work (Call Driver, View Details)
- [ ] Filters work correctly
- [ ] Recent calls feed updates

**Driver Management:**
- [ ] Can add new driver
- [ ] Can edit driver information
- [ ] Can delete driver (with confirmation)
- [ ] Can search drivers
- [ ] Form validations work

**Call Functionality:**
- [ ] Can initiate single call
- [ ] Can initiate bulk calls
- [ ] Call logs are recorded
- [ ] Transcripts are stored
- [ ] Audio recordings accessible (if enabled)

**Analytics:**
- [ ] Charts load correctly
- [ ] Data is accurate
- [ ] Filters work
- [ ] Export functionality works

---

## 📊 DATA GENERATION FOR TESTING

### **Sample Data Sets**

#### **Drivers (10 samples)**
```sql
INSERT INTO drivers (driver_name, phone_number, license_number, email, status) VALUES
('John Smith', '+15551234567', 'DL001234', 'john.smith@email.com', 'ACTIVE'),
('Sarah Johnson', '+15551234568', 'DL001235', 'sarah.johnson@email.com', 'ACTIVE'),
('Mike Davis', '+15551234569', 'DL001236', 'mike.davis@email.com', 'ACTIVE'),
('Emily Brown', '+15551234570', 'DL001237', 'emily.brown@email.com', 'ACTIVE'),
('David Wilson', '+15551234571', 'DL001238', 'david.wilson@email.com', 'ACTIVE'),
('Lisa Anderson', '+15551234572', 'DL001239', 'lisa.anderson@email.com', 'ACTIVE'),
('James Taylor', '+15551234573', 'DL001240', 'james.taylor@email.com', 'ACTIVE'),
('Jennifer Martinez', '+15551234574', 'DL001241', 'jennifer.martinez@email.com', 'ACTIVE'),
('Robert Garcia', '+15551234575', 'DL001242', 'robert.garcia@email.com', 'ACTIVE'),
('Maria Rodriguez', '+15551234576', 'DL001243', 'maria.rodriguez@email.com', 'ACTIVE');
```

#### **Trucks (10 samples)**
```sql
INSERT INTO trucks (truck_number, truck_type, capacity_lbs, license_plate, status) VALUES
('TRK-001', 'DRY_VAN', 45000, 'IL-ABC-123', 'AVAILABLE'),
('TRK-002', 'REFRIGERATED', 40000, 'IL-ABC-124', 'AVAILABLE'),
('TRK-003', 'FLATBED', 48000, 'IL-ABC-125', 'AVAILABLE'),
('TRK-004', 'DRY_VAN', 45000, 'IL-ABC-126', 'IN_TRANSIT'),
('TRK-005', 'REFRIGERATED', 40000, 'IL-ABC-127', 'AVAILABLE'),
('TRK-006', 'DRY_VAN', 45000, 'IL-ABC-128', 'AVAILABLE'),
('TRK-007', 'FLATBED', 48000, 'IL-ABC-129', 'MAINTENANCE'),
('TRK-008', 'DRY_VAN', 45000, 'IL-ABC-130', 'IN_TRANSIT'),
('TRK-009', 'REFRIGERATED', 40000, 'IL-ABC-131', 'AVAILABLE'),
('TRK-010', 'TANKER', 50000, 'IL-ABC-132', 'AVAILABLE');
```

#### **Sample Load Scenarios**

**Scenario 1: Loaded and Ready**
```json
{
  "driver_id": 1,
  "is_loaded": true,
  "cargo_type": "Electronics",
  "cargo_description": "Laptops and monitors",
  "cargo_quantity": "20 pallets",
  "weight_lbs": 35000,
  "destination": "Dallas Distribution Center, 1234 Commerce St",
  "load_completed_time": "2024-10-17T09:30:00Z",
  "departure_time": "2024-10-17T09:45:00Z",
  "issues_notes": "None"
}
```

**Scenario 2: Warehouse Delay**
```json
{
  "driver_id": 2,
  "is_loaded": false,
  "delay_reason_category": "WAREHOUSE_DELAY",
  "delay_reason_details": "Long queue at warehouse, 5 trucks ahead",
  "estimated_load_time": "2024-10-17T12:00:00Z",
  "waiting_duration_minutes": 90,
  "trucks_in_queue": 5,
  "is_recurring_issue": true,
  "current_location": "ABC Warehouse, Chicago"
}
```

**Scenario 3: Mechanical Issue**
```json
{
  "driver_id": 3,
  "is_loaded": false,
  "delay_reason_category": "MECHANICAL_ISSUE",
  "delay_reason_details": "Flat tire, waiting for roadside assistance",
  "estimated_load_time": "2024-10-17T11:30:00Z",
  "waiting_duration_minutes": 45,
  "is_recurring_issue": false,
  "current_location": "Interstate 90, Mile Marker 25"
}
```

**Scenario 4: Paperwork Delay**
```json
{
  "driver_id": 4,
  "is_loaded": false,
  "delay_reason_category": "PAPERWORK",
  "delay_reason_details": "Missing bill of lading, office staff fetching documents",
  "estimated_load_time": "2024-10-17T10:30:00Z",
  "waiting_duration_minutes": 30,
  "is_recurring_issue": false,
  "current_location": "XYZ Shipping Dock, Rockford"
}
```

---

## 🔮 FUTURE ENHANCEMENTS

### **Phase 2 Features (Post-MVP)**

1. **Predictive Analytics**
   - Machine learning model to predict delays
   - Suggest alternative routes/warehouses
   - Optimize call timing based on patterns

2. **Advanced Scheduling**
   - Smart call scheduling (avoid driver rest hours)
   - Timezone-aware calling
   - Retry logic for missed calls

3. **Integration Capabilities**
   - GPS tracking integration
   - Electronic Logging Device (ELD) integration
   - Fuel card integration
   - Customer portal API

4. **Communication Enhancements**
   - SMS fallback if call fails
   - Email summaries
   - WhatsApp integration
   - Multi-language support

5. **Advanced Dashboard**
   - Interactive map with driver locations
   - Weather overlay
   - Traffic conditions
   - Route optimization suggestions

6. **Compliance Features**
   - Hours of Service (HOS) tracking
   - DOT compliance monitoring
   - Automated violation alerts
   - Document management

7. **Mobile App**
   - Native iOS/Android apps for drivers
   - Quick status updates
   - Push notifications
   - Offline mode

8. **AI Improvements**
   - Sentiment analysis of calls
   - Automatic issue categorization
   - Voice biometric authentication
   - Natural language processing for better understanding

---

## 🎓 LEARNING RESOURCES

### **VAPI.ai**
- Documentation: https://docs.vapi.ai
- YouTube Channel: Search "VAPI AI tutorial"
- Discord Community: Join for support

### **FastAPI**
- Official Docs: https://fastapi.tiangolo.com
- Tutorial: https://fastapi.tiangolo.com/tutorial

### **React + Vite**
- Vite Docs: https://vitejs.dev
- React Docs: https://react.dev

### **PostgreSQL**
- Official Docs: https://www.postgresql.org/docs
- Tutorial: https://www.postgresqltutorial.com

### **Trucking Industry Terms**
- TMS: Transportation Management System
- Load: Cargo being transported
- Dispatch: Assignment of loads to drivers
- BOL: Bill of Lading (shipping document)
- ELD: Electronic Logging Device
- HOS: Hours of Service regulations
- Deadhead: Empty truck miles
- LTL: Less Than Truckload
- FTL: Full Truckload

---

## 📝 DELIVERABLES CHECKLIST

### **Code Deliverables**
- [ ] Complete backend codebase (FastAPI)
- [ ] Complete frontend codebase (React + Vite)
- [ ] Database schema SQL files
- [ ] Environment configuration examples
- [ ] README.md with setup instructions

### **Documentation**
- [ ] API documentation (Swagger/Postman collection)
- [ ] Database schema diagram
- [ ] System architecture diagram
- [ ] User guide for dashboard
- [ ] VAPI configuration guide

### **Testing**
- [ ] Unit test suite (backend)
- [ ] Component tests (frontend)
- [ ] Integration test results
- [ ] Manual testing checklist (completed)

### **Deployment**
- [ ] Deployed backend URL
- [ ] Deployed frontend URL
- [ ] Production database credentials
- [ ] VAPI assistant configured

### **Presentation**
- [ ] PowerPoint/Google Slides presentation
- [ ] Demo video (3-5 minutes)
- [ ] Live demo preparation

---

## 🎤 PRESENTATION OUTLINE

### **Slide 1: Title**
- Your Name
- Hemut Load Status Voice AI Agent
- Date

### **Slide 2: Problem Statement**
- Trucking industry statistics (74% on paper)
- Manual dispatch calls are time-consuming
- No real-time visibility
- Costly inefficiencies

### **Slide 3: Solution Overview**
- AI-powered outbound calling
- Automated data collection
- Real-time dashboard
- Pattern analysis

### **Slide 4: Technical Architecture**
- System diagram
- Tech stack: VAPI, FastAPI, React, PostgreSQL
- How components interact

### **Slide 5: Key Features**
- Outbound AI calls
- Intelligent conversation flow
- Automated data storage
- Real-time dashboard
- Analytics & insights

### **Slide 6: Demo**
- Live demonstration
- Show dashboard
- Trigger a call
- Show data updates

### **Slide 7: Database Design**
- Schema diagram
- Key tables
- Relationships

### **Slide 8: VAPI Integration**
- How VAPI works
- Conversation flow
- Function calling
- Webhooks

### **Slide 9: Results & Impact**
- Time saved per dispatcher
- Cost savings
- Improved visibility
- Better decision-making

### **Slide 10: Future Enhancements**
- Predictive analytics
- Mobile app
- GPS integration
- Multi-language support

### **Slide 11: Challenges & Learnings**
- Technical challenges faced
- How you solved them
- What you learned

### **Slide 12: Thank You**
- Questions?
- Contact information
- GitHub repository link

---

## 📞 SUPPORT & CONTACT

**Hemut Team:**
- Company Website: https://www.hemut.com
- Phone: 559-944-7199

**Technical Support:**
- VAPI Discord: https://discord.gg/vapi
- FastAPI GitHub: https://github.com/tiangolo/fastapi
- Stack Overflow

**Your Mentor:**
- Ashish (mention his role)
- Schedule regular check-ins
- Ask questions early and often

---

## ✅ FINAL CHECKLIST

### **Before Starting:**
- [ ] Read this entire document
- [ ] Set up development environment
- [ ] Create VAPI account
- [ ] Install all dependencies
- [ ] Create project folder structure

### **During Development:**
- [ ] Follow the roadmap timeline
- [ ] Test each component individually
- [ ] Commit code regularly to Git
- [ ] Document as you build
- [ ] Ask for help when stuck

### **Before Submission:**
- [ ] All features working
- [ ] No critical bugs
- [ ] Code is clean and commented
- [ ] README is complete
- [ ] Presentation is ready
- [ ] Demo is rehearsed

---

## 🎯 SUCCESS CRITERIA

Your assignment will be evaluated on:

1. **Functionality (40%)**
   - All core features working
   - VAPI integration successful
   - Data correctly stored
   - Dashboard updates in real-time

2. **Code Quality (25%)**
   - Clean, readable code
   - Proper error handling
   - Good project structure
   - Comments and documentation

3. **User Experience (20%)**
   - Intuitive dashboard
   - Good visual design
   - Responsive layout
   - Smooth interactions

4. **Understanding (15%)**
   - Clear presentation
   - Can explain technical choices
   - Understands the business problem
   - Demonstrates learning

---

## 💪 MOTIVATIONAL NOTE

This is an exciting project that solves a real problem in a huge industry! You're building something that could actually save companies thousands of dollars and improve driver experiences.

**Remember:**
- It's okay to not know everything - you're learning!
- Ask questions when confused
- Break big problems into smaller steps
- Test frequently
- Celebrate small wins
- You've got this! 🚀

**Pro Tips:**
1. Start with the simplest version first (MVP)
2. Get one complete flow working end-to-end
3. Then add features incrementally
4. Don't try to build everything at once
5. Focus on making core features work perfectly

Good luck! This is going to be an amazing project for your portfolio!

---

**Document Version:** 1.0  
**Last Updated:** October 17, 2024  
**Prepared For:** Hemut Internship Assignment  
**Total Estimated Time:** 15-17 days