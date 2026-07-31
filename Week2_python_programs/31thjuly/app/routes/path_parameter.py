#path_parameter

from fastapi import APIRouter
from app.database import students

router = APIRouter()

@router.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}