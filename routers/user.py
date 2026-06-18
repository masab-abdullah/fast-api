from fastapi import APIRouter
from models.user import Student ,student1
from crud.student import get_students, add_student
from fastapi import Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from sqlalchemy import text

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Home page"}

@router.get("/info")
def info():
    return {
        "api_name": "FastAPI Basics",
        "version": "1.0",
        "status": "running"
    }
@router.get("/student")
def get_student():
    return student1

@router.get("/students")
def read_students():
    return get_students()

@router.post("/students")
def create_student(student: Student):
    return add_student(student.dict())


@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM student"))
    rows = result.fetchall()
    return [dict(row._mapping) for row in rows]