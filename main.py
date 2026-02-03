from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Job Tracker API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

