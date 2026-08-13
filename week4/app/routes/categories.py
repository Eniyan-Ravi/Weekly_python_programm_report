from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Category
from app.schema import CategoryCreate, CategoryOut
from typing import List
from app.exist_404 import id_404



router = APIRouter(prefix="/categories", tags=["Categories"])



@router.post("/", response_model=CategoryOut)
def create_category(category_request: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(**category_request.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.get("/", response_model=List[CategoryOut])
def get_categoryies(db: Session = Depends(get_db)):
    category = select(Category)
    result = db.execute(category)
    return result.scalars().all()


@router.get("/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return id_404(db, Category, category_id, "Category")


@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int,category_request: CategoryCreate, db: Session = Depends(get_db)):
    
    categor = id_404(db, Category, category_id, "Category")

    categor.name = category_request.name
    categor.type = category_request.type
    db.commit()
    db.refresh(categor)
    return categor


@router.delete("/{category_id}")
def delete_category(category_id: int, db:Session = Depends(get_db)):
    catego = id_404(db, Category, category_id, "Category")
    db.delete(catego)
    db.commit()

    return{
         "message":"Category has been deleted"
    }