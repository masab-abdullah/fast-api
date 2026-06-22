from fastapi import APIRouter 
from schemas.student import StudentCreate, StudentUpdate
from database.postgres_connection import (
    test_postgres_connection,
    PostgresSessionLocal,
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


@router.post("/postgres-students")
def create_postgres_student(student: StudentCreate):
    db = PostgresSessionLocal()

    try:
        query = text("""
            INSERT INTO student (name, age, course)
            VALUES (:name, :age, :course)
        """)

        db.execute(
            query,
            {
                "name": student.name,
                "age": student.age,
                "course": student.course,
            },
        )

        db.commit()

        return {
            "message": "Student added successfully",
            "student": student,
        }

    finally:
        db.close()




@router.patch("/postgres-students/{student_id}")
def update_postgres_student(student_id: int, student: StudentUpdate):
    db = PostgresSessionLocal()

    try:
        query = text("""
            UPDATE student
            SET
                name = COALESCE(:name, name),
                age = COALESCE(:age, age),
                course = COALESCE(:course, course)
            WHERE id = :student_id
        """)

        db.execute(
            query,
            {
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "student_id": student_id
            }
        )

        db.commit()

        return {
            "message": "Student updated successfully",
            "student_id": student_id
        }

    finally:
        db.close()