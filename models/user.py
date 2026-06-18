from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str


student1 = Student(
    name="gsd",
    age=19,
    course="BSCS"
)