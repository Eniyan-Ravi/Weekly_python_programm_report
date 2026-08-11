from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import PaymentMethod, User
from app.schema import PaymentMethodCreate, PaymentMethodOut, PaymentMethodUpdate
from typing import List



router = APIRouter(prefix="/payment_methods", tags=["Payment Methods"])
@router.post("/", response_model=PaymentMethodOut)
def create_patmat(Paymat_request: PaymentMethodCreate, db: Session = Depends(get_db)):
    user_stmt = select(User).where(User.id == Paymat_request.user_id)
    exist_user=db.execute(user_stmt).scalar_one_or_none()
    if exist_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")

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
    paym = select(PaymentMethod).where(PaymentMethod.id == pay_method_id)
    search = db.execute(paym).scalar_one_or_none()
    if search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment Method not found")
    return search


@router.put("/{pay_method_id}", response_model=PaymentMethodOut)
def update_pay_method(pay_method_id: int, paym_request: PaymentMethodUpdate, db: Session = Depends(get_db)):
    paymet = select(PaymentMethod).where(PaymentMethod.id == pay_method_id)
    updat = db.execute(paymet).scalar_one_or_none()

    if updat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment Method not found")

    updat.type = paym_request.type
    updat.provider_name = paym_request.provider_name
    updat.is_default = paym_request.is_default
    db.commit()
    db.refresh(updat)
    return updat


@router.delete("/{pay_method_id}")
def delete_pay_method(pay_method_id: int, db:Session = Depends(get_db)):
    paymet= select(PaymentMethod).where(PaymentMethod.id == pay_method_id)
    dele = db.execute(paymet).scalar_one_or_none()
    if dele is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(dele)
    db.commit()

    return{
         "message":"Payment Method has been deleted"
    }