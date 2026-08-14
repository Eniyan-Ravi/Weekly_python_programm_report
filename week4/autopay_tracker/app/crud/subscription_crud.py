from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Subscription

def get_by_id(db: Session, sub_id: int):
    stmt = select(Subscription).where(Subscription.id == sub_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result

def get_all(db: Session):
    return db.execute(select(Subscription)).scalars().all()

def create(db: Session, subscription: Subscription):
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription

def update(db: Session, subscription: Subscription):
    db.commit()
    db.refresh(subscription)
    return subscription

def delete(db: Session, subscription: Subscription):
    db.delete(subscription)
    db.commit()