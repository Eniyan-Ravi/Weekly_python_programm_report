from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import User
from app.schema import UserCreate, UserOut, UserUpdate
from typing import List
from app.exist_404 import id_404


router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user_request: UserCreate, db: Session = Depends(get_db)):
    user = User(**user_request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    user = select(User)
    result = db.execute(user)
    return result.scalars().all()

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return id_404(db, User, user_id, "User")


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int,user_request: UserUpdate, db: Session = Depends(get_db)):
    user = id_404(db, User, user_id, "User")
    user.name = user_request.name
    user.email = user_request.email
    user.phone = user_request.phone
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    user = id_404(db, User, user_id, "User")
    db.delete(user)
    db.commit()

    return{
         "message":"User has been deleted"
    }