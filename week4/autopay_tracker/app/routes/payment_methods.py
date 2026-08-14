from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import PaymentMethodCreate, PaymentMethodOut, PaymentMethodUpdate
from app.services import payment_method_service

router = APIRouter(prefix="/payment_methods", tags=["Payment Methods"])

@router.post("/", response_model=PaymentMethodOut)
def create_payment_method(payment_request: PaymentMethodCreate, db: Session = Depends(get_db)):
    return payment_method_service.create_payment_method(db, payment_request)

@router.get("/", response_model=List[PaymentMethodOut])
def get_payment_methods(db: Session = Depends(get_db)):
    return payment_method_service.list_payment_methods(db)

@router.get("/{pay_method_id}", response_model=PaymentMethodOut)
def get_payment_method(pay_method_id: int, db: Session = Depends(get_db)):
    return payment_method_service.get_payment_method(db, pay_method_id)

@router.put("/{pay_method_id}", response_model=PaymentMethodOut)
def update_payment_method(pay_method_id: int, payment_request: PaymentMethodUpdate, db: Session = Depends(get_db)):
    return payment_method_service.update_payment_method(db, pay_method_id, payment_request)

@router.delete("/{pay_method_id}")
def delete_payment_method(pay_method_id: int, db: Session = Depends(get_db)):
    payment_method_service.delete_payment_method(db, pay_method_id)
    return {"message": "Payment Method has been deleted"}