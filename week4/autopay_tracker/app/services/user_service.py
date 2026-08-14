from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserUpdate
from app.utility import require_exists
from app.crud import user_crud

def create_user(db: Session, request: UserCreate):
    user = User(**request.model_dump())
    return user_crud.create(db, user)

def get_user(db: Session, user_id: int):
    return require_exists(db, User, user_id, "User")

def list_users(db: Session):
    return user_crud.get_all(db)

def update_user(db: Session, user_id: int, request: UserUpdate):
    user = require_exists(db, User, user_id, "User")
    user.name = request.name
    user.email = request.email
    user.phone = request.phone
    return user_crud.update(db, user)

def delete_user(db: Session, user_id: int):
    user = require_exists(db, User, user_id, "User")
    user_crud.delete(db, user)