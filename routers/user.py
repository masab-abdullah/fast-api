from fastapi import APIRouter
from models.user import student

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
def student():
    return {
        "name": "Ali",
        "age": 18,
        "course": "BSCS"
    }