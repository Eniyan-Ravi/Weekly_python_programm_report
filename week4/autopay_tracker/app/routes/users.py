from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import UserCreate, UserOut, UserUpdate
from app.services import user_service

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user_request: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user_request)

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.list_users(db)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, user_id)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_request: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user_request)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
    return {"message": "User has been deleted"}