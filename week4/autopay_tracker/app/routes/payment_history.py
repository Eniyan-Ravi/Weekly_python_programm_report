from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import PaymentHistoryCreate, PaymentHistoryOut
from app.services import payment_history_service

router = APIRouter(prefix="/payment_history", tags=["Payment History"])

@router.post("/", response_model=PaymentHistoryOut)
def create_payment_history(payhistory_request: PaymentHistoryCreate, db: Session = Depends(get_db)):
    return payment_history_service.create_payment_history(db, payhistory_request)

@router.get("/", response_model=List[PaymentHistoryOut])
def get_payment_histories(db: Session = Depends(get_db)):
    return payment_history_service.list_payment_histories(db)

@router.get("/{payhistory_id}", response_model=PaymentHistoryOut)
def get_payment_history(payhistory_id: int, db: Session = Depends(get_db)):
    return payment_history_service.get_payment_history(db, payhistory_id)