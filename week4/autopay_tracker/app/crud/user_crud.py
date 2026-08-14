from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User

def get_by_id(db: Session, user_id: int):
    stmt = select(User).where(User.id == user_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result

def get_all(db: Session):
    return db.execute(select(User)).scalars().all()

def create(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update(db: Session, user: User):
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, user: User):
    db.delete(user)
    db.commit()