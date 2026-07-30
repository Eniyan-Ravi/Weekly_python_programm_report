#student
from fastapi import FastAPI

app = FastAPI()

# List to store students
students = []

# Add a student
@app.post("/students")
def add_student(student: dict):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }

# Get all students
@app.get("/students")
def get_all_students():
    return students

# Get one student using ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}