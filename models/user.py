from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str


student1 = Student(
    name="masab",
    age=19,
    course="BSCS"
)