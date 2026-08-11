from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Category
from app.schema import CategoryCreate, CategoryOut
from typing import List



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
    category = select(Category).where(Category.id == category_id)
    category = db.execute(category).scalar_one_or_none()
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return category


@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int,category_request: CategoryCreate, db: Session = Depends(get_db)):
    cat = select(Category).where(Category.id == category_id)
    categor = db.execute(cat).scalar_one_or_none()

    if categor is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    categor.name = category_request.name
    categor.type = category_request.type
    db.commit()
    db.refresh(categor)
    return categor


@router.delete("/{category_id}")
def delete_category(category_id: int, db:Session = Depends(get_db)):
    cate= select(Category).where(Category.id == category_id)
    catego = db.execute(cate).scalar_one_or_none()
    if catego is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(catego)
    db.commit()

    return{
         "message":"Category has been deleted"
    }