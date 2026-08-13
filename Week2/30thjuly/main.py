from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/student")
def student():
    return {
        "name": "John",
        "age": 20
    }

@app.post("/add")
def add_student(student: dict):
    return {
        "received": student
    }