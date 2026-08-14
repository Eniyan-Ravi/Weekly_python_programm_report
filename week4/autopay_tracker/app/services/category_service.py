from sqlalchemy.orm import Session
from app.models import Category
from app.schema import CategoryCreate
from app.utility import require_exists
from app.crud import category_crud

def create_category(db: Session, request: CategoryCreate):
    category = Category(**request.model_dump())
    return category_crud.create(db, category)

def get_category(db: Session, category_id: int):
    return require_exists(db, Category, category_id, "Category")

def list_categories(db: Session):
    return category_crud.get_all(db)

def update_category(db: Session, category_id: int, request: CategoryCreate):
    category = require_exists(db, Category, category_id, "Category")
    category.name = request.name
    category.type = request.type
    return category_crud.update(db, category)

def delete_category(db: Session, category_id: int):
    category = require_exists(db, Category, category_id, "Category")
    category_crud.delete(db, category)