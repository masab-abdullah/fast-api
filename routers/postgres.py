from fastapi import APIRouter
from database.postgres_connection import (
    test_postgres_connection,
    PostgresSessionLocal
)

from sqlalchemy import text
router = APIRouter()

@router.get("/postgres-check")
def postgres_check():
    result = test_postgres_connection()

    return {
        "database": result[0]
    }
@router.get("/postgres-students")
def get_postgres_students():
    db = PostgresSessionLocal()

    try:
        result = db.execute(text("SELECT * FROM student"))
        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]

    finally:
        db.close()