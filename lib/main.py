#  write your solution here
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import desc, asc
from lib.models.employee import session, Employee
app = FastAPI()

class EmployeeSchema(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    age:int
    gender:str
    phone_number:int
    salary: int
    designation:str
    class Config:
        orm_mode = True


@app.get('/employees')
def root() -> List[EmployeeSchema]:
    employee = session.query(Employee).all()
    return employee

@app.get("/employees/{id}")
def get_student_single(id: int):
    employee = session.query(Employee).filter_by(id=id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist in our databse")
    return employee
@app.get("/employees/salary/asc")
def get_employees_sorted_by_salary():
    sorted_employees = session.query(Employee).order_by(asc(Employee.salary)).all()
    return sorted_employees

@app.get("/employees/age/old") 
def get_oldest_employee():
    oldest_employee = session.query(Employee).order_by(desc(Employee.age)).first()
    return oldest_employee






