from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import User
from app.schema import UserCreate, UserOut, UserUpdate
from typing import List



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
    user = select(User).where(User.id == user_id)
    use = db.execute(user).scalar_one_or_none()
    if use is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return use


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int,user_request: UserUpdate, db: Session = Depends(get_db)):
    us = select(User).where(User.id == user_id)
    user = db.execute(us).scalar_one_or_none()

    if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    user.name = user_request.name
    user.email = user_request.email
    user.phone = user_request.phone
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    use= select(User).where(User.id == user_id)
    us = db.execute(use).scalar_one_or_none()
    if us is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(us)
    db.commit()

    return{
         "message":"User has been deleted"
    }