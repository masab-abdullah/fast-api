from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:kawasaki@localhost:5432/college"

postgres_engine = create_engine(DATABASE_URL)

PostgresSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=postgres_engine
)

def test_postgres_connection():
    db = PostgresSessionLocal()

    try:
        result = db.execute(text("SELECT current_database();"))
        return result.fetchone()

    finally:
        db.close()