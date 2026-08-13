#main
from typing import Annotated
from pydantic import Field
from sqlalchemy.orm import Session 
from fastapi import FastAPI, Depends, HTTPException, Path, status
from app import model
from app.model import Todos
from app.database import engine, SessionLocal

app = FastAPI()

model.Base.metadata.create_all(bind=engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def real_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int=Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model 
    raise HTTPException(status_code=404, detail='Todo not found.')

