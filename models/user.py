from pydantic import BaseModel

class student(BaseModel):
    name: str
    age: int
    course: str