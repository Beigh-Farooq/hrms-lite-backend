# HRMS Lite – Backend

## Project Description
HRMS Lite Backend is a RESTful API built to support a lightweight Human Resource Management System.
It allows an admin to:
- Manage employee records
- Track daily attendance (Present / Absent)

The backend is designed to be simple, stable, focusing only on core HR operations as required by the assignment.

---

## Tech Stack Used
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic (validation)
- Uvicorn (ASGI server)

---

## Features Implemented
- Add / list / delete employees
- Mark daily attendance
- View attendance records per employee
- Server-side validation
- Proper HTTP status codes
- Meaningful error responses
- PostgreSQL persistence

---

## Prerequisites
Make sure you have the following installed locally:

- Python 3.9+
- PostgreSQL
- pip (Python package manager)
- Git

---

##  Local Setup Instructions

### 1️ Clone the repository
    git clone https://github.com/<your-username>/hrms-lite-backend.git
    cd hrms-lite-backend

### 2️ Create & activate virtual environment
    python -m venv venv
    venv\Scripts\activate

### 3️ Install dependencies
    pip install -r requirements.txt

### 4️ Setup PostgreSQL Database
    Login to PostgreSQL:
    psql postgres

    Create database and user:

    CREATE DATABASE hrms_lite;
    CREATE USER hrms_user WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE hrms_lite TO hrms_user;


### 5️ Create .env file
    Create a file named .env in the project root:
    DATABASE_URL=postgresql://hrms_user:password@localhost:5432/hrms_lite

### 6️ Run the server
    uvicorn app.main:app --reload

