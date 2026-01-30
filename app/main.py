from fastapi import FastAPI
from app.database import engine, Base 
from app import models 

app = FastAPI(title="HRMS Lite API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "HRMS Lite Backend Running"}