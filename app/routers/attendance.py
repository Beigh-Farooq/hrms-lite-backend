from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from datetime import date

router = APIRouter(prefix="/attendance",tags=["Attendance"])


# Mark Attendance API (POST /attendance)
# Employee must exist
# Only one attendance record per employee per date
# Proper error messages
@router.post("",status_code=status.HTTP_201_CREATED)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    # Check employee exists
    employee = db.query(models.Employee).filter(
        models.Employee.employee_id == attendance.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    # Check duplicate attendance for same date
    existing_record = db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee.id,
        models.Attendance.date == attendance.date
    ).first()

    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Attendance already marked for this date"
        )

    new_attendance = models.Attendance(
        employee_id=employee.id,
        date=attendance.date,
        status=models.AttendanceStatus(attendance.status)
    )

    db.add(new_attendance)
    db.commit()

    return {"message": "Attendance marked successfully"}







# View Attendance API (GET /attendance/{employee_id})
@router.get("/{employee_id}", response_model=schemas.EmployeeAttendanceResponse)
def get_attendance(employee_id: str, db: Session = Depends(get_db) ):
    employee = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    records = db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee.id
    ).order_by(models.Attendance.date.desc()).all()

    return {
        "employee_id": employee.employee_id,
        "records": records
    }
