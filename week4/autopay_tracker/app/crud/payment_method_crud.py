from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import PaymentMethod

def get_by_id(db: Session, pay_method_id: int):
    stmt = select(PaymentMethod).where(PaymentMethod.id == pay_method_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result

def get_all(db: Session):
    
    return db.execute(select(PaymentMethod)).scalars().all()

def create(db: Session, payment_method: PaymentMethod):
    db.add(payment_method)
    db.commit()
    db.refresh(payment_method)
    return payment_method

def update(db: Session, payment_method: PaymentMethod):
    db.commit()
    db.refresh(payment_method)
    return payment_method

def delete(db: Session, payment_method: PaymentMethod):
    db.delete(payment_method)
    db.commit()