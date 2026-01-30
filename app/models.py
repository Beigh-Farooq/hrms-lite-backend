from sqlalchemy import Column,String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship 
from app.database import Base 
import enum 
import uuid 

class Employee(Base):
    __tablename__="employees"

    id = Column(String,primary_key=True,default=lambda:str(uuid.uuid4()))
    employee_id= Column(String,unique=True,nullable=False)
    full_name=Column(String,nullable=False)
    email= Column(String, unique=True,nullable=False)
    department = Column(String,nullable=False)

    attendance_records= relationship(
        "Attendance",
        back_populates="employee",
        cascade="all, delete"
    )

class AttendanceStatus(enum.Enum):
    PRESENT = "Present"
    ABSENT = "Absent"

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))
    employee_id = Column(String, ForeignKey("employees.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), nullable=False)

    employee = relationship("Employee", back_populates="attendance_records")