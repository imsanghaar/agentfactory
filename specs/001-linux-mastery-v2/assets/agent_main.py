"""
Sample AI Agent for Linux Mastery Chapter
==========================================
A minimal FastAPI agent used throughout Chapter 10 to practice
deployment, monitoring, and management on Linux servers.

Requirements: pip install fastapi uvicorn
Run directly: uvicorn agent_main:app --host 0.0.0.0 --port 8000
"""

from datetime import datetime
from fastapi import FastAPI

# Create the FastAPI application
# This is the "agent" that we'll deploy as a systemd service
app = FastAPI(
    title="Sample Digital FTE Agent",
    description="A minimal agent for practicing Linux deployment skills",
    version="1.0.0"
)

# Health check endpoint
# Used by monitoring scripts to verify the agent is alive
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "agent": "running",
        "timestamp": datetime.now().isoformat()
    }

# Sample task endpoint
# Represents the agent's actual work (simplified for learning)
@app.get("/tasks")
def list_tasks():
    return {
        "tasks": [
            {"id": 1, "name": "Process customer inquiry", "status": "pending"},
            {"id": 2, "name": "Generate daily report", "status": "completed"},
            {"id": 3, "name": "Update knowledge base", "status": "in_progress"}
        ],
        "total": 3,
        "agent_uptime": "running since startup"
    }

# Entry point when running directly (not via uvicorn command)
if __name__ == "__main__":
    import uvicorn
    # Host 0.0.0.0 makes agent accessible from network (not just localhost)
    # Port 8000 is the default for development
    uvicorn.run(app, host="0.0.0.0", port=8000)
