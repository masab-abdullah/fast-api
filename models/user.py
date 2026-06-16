from pydantic import BaseModel

class student(BaseModel):
    name: str
    age: int
    course: str


student1 = student(
    name="masab",
    age=19,
    course="BSCS"
)