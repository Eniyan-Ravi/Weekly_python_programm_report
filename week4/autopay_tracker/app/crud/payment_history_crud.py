from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import PaymentHistory

def get_by_id(db: Session, payhistory_id: int):
    stmt = select(PaymentHistory).where(PaymentHistory.id == payhistory_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result


def get_all(db: Session):
    return db.execute(select(PaymentHistory)).scalars().all()

def create(db: Session, payhistory: PaymentHistory):
    db.add(payhistory)
    db.commit()
    db.refresh(payhistory)
    return payhistory