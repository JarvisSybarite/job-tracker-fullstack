# Job Application Tracker API

Backend service for a job application tracking system.
This API will support creating, updating, and tracking job applications through different stages.

## Features
- REST API built with FastAPI
- Health check endpoint
- Auto-generated API documentation (Swagger UI)
- Structured for future database and authentication integration

## Tech Stack
- Python 3
- FastAPI
- Uvicorn

## API Endpoints

Method | Endpoint | Description
GET    | /        | Root status check
GET    | /health  | Service health check

## API Docs Preview
![FastAPI Swagger UI](docs/api-docs.png)

## How to Run Locally

Create virtual environment:
python3 -m venv venv

Activate it:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000

API documentation:
http://127.0.0.1:8000/docs

## Project Status
In progress — next steps include database integration and CRUD endpoints for job applications.
