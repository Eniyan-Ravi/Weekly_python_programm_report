#delete_student
from fastapi import APIRouter
from app.database import students

router = APIRouter()

@router.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully",
                "student": student
            }

    return {"message": "Student not found"}