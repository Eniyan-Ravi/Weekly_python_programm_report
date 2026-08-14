from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import EMI

def get_by_id(db: Session, emi_id: int):
    stmt = select(EMI).where(EMI.id == emi_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result

def get_all(db: Session):
    stmt = select(EMI)
    result = db.execute(stmt).scalars().all()
    return result

def create(db: Session, emi: EMI):
    db.add(emi)
    db.commit()
    db.refresh(emi)
    return emi

def update(db: Session, emi: EMI):
    db.commit()
    db.refresh(emi)
    return emi

def delete(db: Session, emi: EMI):
    db.delete(emi)
    db.commit()