from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import employees, attendance
import os

app = FastAPI(title="HRMS Lite API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Get frontend URL from environment variable (optional)
frontend_url = os.getenv("FRONTEND_URL")

# Explicit allowed origins
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://hrms-lite-frontend.vercel.app",   # production URL
]

# Add env-based frontend URL if exists
if frontend_url:
    origins.append(frontend_url)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://hrms-lite-frontend.*\.vercel\.app",  # allow all Vercel previews
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(employees.router)
app.include_router(attendance.router)

# Root endpoint
@app.get("/")
def root():
    return {"status": "HRMS Lite Backend Running"}