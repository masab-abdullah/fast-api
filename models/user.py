from sqlalchemy import Column, Integer, String
from database.postgres_connection import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)
    email = Column(String)