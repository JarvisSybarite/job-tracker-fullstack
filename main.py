from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

applications_db = []

class JobApplication(BaseModel):
    company: str
    role: str
    status: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Job Tracker API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/applications")
def create_application(application: JobApplication):
    applications_db.append(application)
    return {"created": True, "application": application}
@app.get("/applications")
def list_applications():
    return applications_db


