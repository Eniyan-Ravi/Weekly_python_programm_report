from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Category

def get_by_id(db: Session, category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result


def get_all(db: Session):
    return db.execute(select(Category)).scalars().all()


def create(db: Session, category: Category):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update(db: Session, category: Category):
    db.commit()
    db.refresh(category)
    return category

def delete(db: Session, category: Category):
    db.delete(category)
    db.commit()