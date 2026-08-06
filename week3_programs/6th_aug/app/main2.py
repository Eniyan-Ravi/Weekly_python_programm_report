#main2
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import model

app = FastAPI(title="Todo API - Main2")

model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", status_code=status.HTTP_200_OK)
def read_all(db: Session = Depends(get_db)):
    stmt = select(model.Todos)
    result = db.execute(stmt)
    todos = result.scalars().all()
    return todos


@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    stmt = select(model.Todos).where(model.Todos.id == todo_id)
    todo = db.execute(stmt).scalar_one_or_none()

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


@app.get("/todos/priority/{priority}", status_code=status.HTTP_200_OK)
def read_priority(priority: int, db: Session = Depends(get_db)):
    stmt = select(model.Todos).where(model.Todos.priority == priority)
    todos = db.execute(stmt).scalars().all()

    if not todos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return todos


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(title: str,
                description: str,
                priority: int,
                complete: bool,
                db: Session = Depends(get_db)):

    todo = model.Todos(
        title=title,
        description=description,
        priority=priority,
        complete=complete
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


@app.put("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def update_todo(todo_id: int,
                title: str,
                description: str,
                priority: int,
                complete: bool,
                db: Session = Depends(get_db)):

    stmt = select(model.Todos).where(model.Todos.id == todo_id)
    todo = db.execute(stmt).scalar_one_or_none()

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = title
    todo.description = description
    todo.priority = priority
    todo.complete = complete

    db.commit()
    db.refresh(todo)

    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):

    stmt = select(model.Todos).where(model.Todos.id == todo_id)
    todo = db.execute(stmt).scalar_one_or_none()

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND)

    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted successfully"}