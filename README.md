# Log Processing API (FastAPI)

A simple FastAPI-based service that processes and analyzes log data.

It parses raw logs, converts them into structured format, and provides statistics like success/failure count, most active user, and action frequency.

---

# Features

- Parse log strings into structured JSON
- Count success and failed logs
- Find most active user
- Count action frequency
- Detect malformed logs safely

---

# Tech Stack

- Python
- FastAPI
- Pydantic
- Collections (Counter)

---

# Log Format

Each log must follow this format:

timestamp|user_id|action|status

Example:

2026-05-01 10:00:00|user_1|login|success  
2026-05-01 10:05:00|user_2|purchase|failed

---

# Installation

## Step 1: Clone project

git clone https://github.com/sindhurametla/logparsing.git  
cd logparsing.git  

## Step 2: Create virtual environment

python -m venv venv  

## Step 3: Activate virtual environment

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

## Step 4: Install dependencies

pip install fastapi uvicorn  

---

# Run the project

uvicorn main:app --reload  

Open in browser:

http://127.0.0.1:8000  

---

# API Endpoint

POST /process_logs

---

# Request Example

{
  "logs": [
    "2026-05-01 10:00:00|user_1|login|success",
    "2026-05-01 10:05:00|user_2|purchase|failed"
  ]
}

---

# Response Example

{
  "success": 1,
  "failed": 1,
  "most_active_user": "user_1",
  "action_frequency": {
    "login": 1,
    "purchase": 1
  },
  "structured_logs": [
    {
      "timestamp": "2026-05-01 10:00:00",
      "user": "user_1",
      "action": "login",
      "status": "success"
    }
  ],
  "malformed_logs": []
}

---

# How it works

- Reads log list
- Splits each log using "|"
- Converts into dictionary format
- Tracks stats using Counter
- Handles bad logs safely

---

# Error Handling

If a log is not in correct format, it is stored in:

malformed_logs

---

# Author

Sindura Metla

---

# GitHub
https://github.com/sindhurametla/logparsing.git  
