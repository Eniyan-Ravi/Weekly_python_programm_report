from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import PaymentMethod, User
from app.schema import PaymentMethodCreate, PaymentMethodOut, PaymentMethodUpdate
from typing import List
from app.utility import require_exists



router = APIRouter(prefix="/payment_methods", tags=["Payment Methods"])



@router.post("/", response_model=PaymentMethodOut)
def create_patmat(Paymat_request: PaymentMethodCreate, db: Session = Depends(get_db)):
    exist_user = require_exists(db, User, Paymat_request.user_id, "User")

    paymentmethod = PaymentMethod(**Paymat_request.model_dump())
    db.add(paymentmethod)
    db.commit()
    db.refresh(paymentmethod)
    return paymentmethod


@router.get("/", response_model=List[PaymentMethodOut])
def get_pay_methods(db: Session = Depends(get_db)):
    pay_met = select(PaymentMethod)
    result = db.execute(pay_met)
    return result.scalars().all()


@router.get("/{pay_method_id}", response_model=PaymentMethodOut)
def get_pay_method(pay_method_id: int, db: Session = Depends(get_db)):
    return require_exists(db, PaymentMethod, pay_method_id, "Payment Method")


@router.put("/{pay_method_id}", response_model=PaymentMethodOut)
def update_pay_method(pay_method_id: int, paym_request: PaymentMethodUpdate, db: Session = Depends(get_db)):
    updat = require_exists(db, PaymentMethod, pay_method_id, "Payment Method")

    updat.type = paym_request.type
    updat.provider_name = paym_request.provider_name
    updat.is_default = paym_request.is_default
    db.commit()
    db.refresh(updat)
    return updat


@router.delete("/{pay_method_id}")
def delete_pay_method(pay_method_id: int, db:Session = Depends(get_db)):
    dele = require_exists(db, PaymentMethod, pay_method_id, "Payment Method")
    db.delete(dele)
    db.commit()

    return{
         "message":"Payment Method has been deleted"
    }