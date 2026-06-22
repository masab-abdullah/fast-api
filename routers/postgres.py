from fastapi import APIRouter
from database.postgres_connection import test_postgres_connection

router = APIRouter()

@router.get("/postgres-check")
def postgres_check():
    result = test_postgres_connection()

    return {
        "database": result[0]
    }