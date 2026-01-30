from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List
from enum import Enum


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

class EmployeeResponse(BaseModel):
    id: str
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    class Config:
        from_attributes = True



class AttendanceStatus(str, Enum):
    Present = "Present"
    Absent = "Absent"


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: AttendanceStatus



class AttendanceResponse(BaseModel):
    id: str
    date: date
    status: AttendanceStatus

    class Config:
        from_attributes = True


class EmployeeAttendanceResponse(BaseModel):
    employee_id: str
    records: List[AttendanceResponse]
