from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4


app = FastAPI()

class JobApplicationCreate(BaseModel):
    company: str
    role: str
    status: str

class JobApplication(JobApplicationCreate):
    id: str

applications_db: List[JobApplication] = []

@app.get("/")
def root():
    return {"status": "ok", "message": "Job Tracker API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/applications")
def create_application(application: JobApplicationCreate):
    new_app = JobApplication(
        id=str(uuid4()),
        company=application.company,
        role=application.role,
        status=application.status
    )
    applications_db.append(new_app)
    return {"created": True, "application": new_app}

@app.get("/applications")
def list_applications():
    return applications_db