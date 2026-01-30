from fastapi import FastAPI
from app.database import engine, Base 
from app import models 
from app.routers import employees,attendance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HRMS Lite API")

Base.metadata.create_all(bind=engine)


# CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"status": "HRMS Lite Backend Running"}