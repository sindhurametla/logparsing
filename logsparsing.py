from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from collections import Counter 


app = FastAPI()


class LogParse(BaseModel):
    logs: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "logs": [
                    "2026-05-01 10:00:00|user_1|login|success",
                    "2026-05-01 10:05:00|user_2|purchase|failed"
                ]
            }
        }

@app.post('/process_logs')
def process_logs(request: LogParse):

    success_count = 0 
    failure_count = 0 

    user_counter = Counter()
    action_counter = Counter()
    
    structured_logs = []
    malformed_logs = []

    for log in request.logs:
        try:
            timestamp, user, action, status = log.split('|')

            log_data = {
                "timestamp": timestamp,
                "user": user,
                "action": action,
                "status": status
            }

            structured_logs.append(log_data)
            if status == "success":
                success_count += 1
            else:
                failure_count += 1

            user_counter[user] += 1
            action_counter[action] += 1
        except ValueError:
            malformed_logs.append(log)

    return {
        "success": success_count,
        "failed": failure_count,
        "most_active_user": user_counter.most_common(1)[0][0]
        if user_counter else None,
        "action_frequency": dict(action_counter),
        "structured_logs": structured_logs,
        "malformed_logs": malformed_logs
    }

    
