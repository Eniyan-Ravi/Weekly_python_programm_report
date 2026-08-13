from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Subscription, User, PaymentMethod, Category,EMI, PaymentHistory
from app.schema import PaymentHistoryCreate, PaymentHistoryOut
from typing import List
from app.utility import require_exists

router = APIRouter(prefix="/payment_history", tags=["Payment History"])


@router.post("/", response_model=PaymentHistoryOut)
def create_payhistory(payhistory_request: PaymentHistoryCreate, db: Session = Depends(get_db)):
    user_stmt = select(User).where(User.id == payhistory_request.user_id)
    payment_stmt = select(PaymentMethod).where(PaymentMethod.id == payhistory_request.payment_method_id)

    exist_user = db.execute(user_stmt).scalar_one_or_none()
    exist_payment = db.execute(payment_stmt).scalar_one_or_none()
    if exist_user is None or exist_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    if (payhistory_request.subscription_id is None) == (payhistory_request.emi_id is None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Exactly one of subscription_id or emi_id must be provided"
        )

    if payhistory_request.subscription_id is not None:
        sub_stmt = select(Subscription).where(Subscription.id == payhistory_request.subscription_id)
        exist_sub = db.execute(sub_stmt).scalar_one_or_none()
        if exist_sub is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found")

    if payhistory_request.emi_id is not None:
        emi_stmt = select(EMI).where(EMI.id == payhistory_request.emi_id)
        exist_emi = db.execute(emi_stmt).scalar_one_or_none()
        if exist_emi is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EMI not found")

    payhistory = PaymentHistory(**payhistory_request.model_dump())
    db.add(payhistory)
    db.commit()
    db.refresh(payhistory)
    return payhistory


@router.get("/", response_model=List[PaymentHistoryOut])
def get_paymentHistories(db: Session = Depends(get_db)):
    pay = select(PaymentHistory)
    result = db.execute(pay)
    return result.scalars().all()

@router.get("/{payhistory_id}", response_model=PaymentHistoryOut)
def get_payhistory(payhistory_id: int, db: Session = Depends(get_db)):
    return require_exists(db, PaymentHistory, payhistory_id, "Payment History")