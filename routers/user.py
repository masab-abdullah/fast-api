from fastapi import APIRouter
from models.user import Student ,student1
from crud.student import get_students, add_student

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
