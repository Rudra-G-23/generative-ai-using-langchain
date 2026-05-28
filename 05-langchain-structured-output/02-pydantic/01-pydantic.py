from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name: str = "Rudra"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0, lt=10, default=5, description="A decimal value representing the cgpa"
    )


new_student = {
    "name": "Rudra",
    "age": 20,
    "email": "rudra@gmail.com",
}

new_student = Student(**new_student)

print(new_student)
print(new_student.age)
print(new_student.model_dump_json())
