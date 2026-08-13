#update_student info using put
from fastapi import APIRouter
from app.model import Student
from app.database import students

router = APIRouter()

@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for s in students:
        if s["id"] == student_id:
            s["name"] = student.name
            s["age"] = student.age

            return {
                "message": "Student updated successfully",
                "student": s
            }

    return {"message": "Student not found"}