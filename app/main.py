from fastapi import FastAPI
from app.database import engine, Base 
from app import models 
from app.routers import employees,attendance

app = FastAPI(title="HRMS Lite API")

Base.metadata.create_all(bind=engine)

app.include_router(employees.router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {"status": "HRMS Lite Backend Running"}