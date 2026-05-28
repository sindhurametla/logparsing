# Log Processing & Analytics System

A FastAPI-based system that processes raw application logs, converts them into structured data, and generates analytical insights such as success/failure counts, user activity, and action frequency distribution.

---

## 🚀 Features

- Accepts log data via API
- Parses raw log strings into structured format
- Tracks success and failure events
- Identifies most active users
- Computes action frequency distribution
- Handles malformed log entries safely
- Returns structured analytics response

---

## 🧠 Problem Statement

Modern systems generate large volumes of unstructured logs.  
This project focuses on:

- Converting raw logs into structured format
- Extracting meaningful insights
- Handling inconsistent or malformed data
- Producing clean analytical summaries via API

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Pydantic
- Collections (Counter)
- Uvicorn

---

## 📦 Installation

Install dependencies:

```bash
pip install fastapi uvicorn

▶️ How to Run the Project

Start the FastAPI server:

uvicorn main:app --reload

The application will run at:

http://127.0.0.1:8000

Once started, you can:

Access API endpoints
Test requests via Swagger UI
View live documentation
📚 API Documentation (Swagger UI)

FastAPI automatically generates interactive API docs:

http://127.0.0.1:8000/docs

You can test all endpoints directly in the browser.

📡 API Endpoint
POST /process_logs

This endpoint processes raw log strings and returns structured analytics.

📥 Request Format
{
  "logs": [
    "2026-05-01 10:00:00|user_1|login|success",
    "2026-05-01 10:05:00|user_2|purchase|failed",
    "2026-05-01 10:10:00|user_1|logout|success",
    "2026-05-01 10:15:00|user_3|login|success"
  ]
}
📤 Response Format
{
  "success": 3,
  "failed": 1,
  "most_active_user": "user_1",
  "action_frequency": {
    "login": 2,
    "purchase": 1,
    "logout": 1
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

## 🏗️ System Flow

Client Request  
↓  
FastAPI Endpoint  
↓  
Log Parsing Layer  
↓  
Data Structuring  
↓  
Aggregation (Counter)  
↓  
JSON Response

## 🧪 Example Use Cases

- Application log monitoring  
- User activity tracking  
- Event analytics systems  
- Log processing pipelines  

