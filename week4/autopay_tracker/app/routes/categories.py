from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import CategoryCreate, CategoryOut
from app.services import category_service

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryOut)
def create_category(category_request: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, category_request)

@router.get("/", response_model=List[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return category_service.list_categories(db)

@router.get("/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return category_service.get_category(db, category_id)

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category_request: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.update_category(db, category_id, category_request)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_service.delete_category(db, category_id)
    return {"message": "Category has been deleted"}