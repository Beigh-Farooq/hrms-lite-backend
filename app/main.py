from fastapi import FastAPI

app = FastAPI(title="HRMS Lite API")

@app.get("/")
def root():
    return {"status": "HRMS Lite Backend Running"}