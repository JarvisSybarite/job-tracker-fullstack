from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
    return {"created": True, "application": application}

