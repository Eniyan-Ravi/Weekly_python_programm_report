from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import PaymentMethod, User, Category,EMI
from app.schema import EMICreate, EMIOut, EMIUpdate
from typing import List

router = APIRouter(prefix="/emis", tags=["EMI"])

@router.post("/", response_model=EMIOut)
def create_emis(Emi_request: EMICreate, db: Session = Depends(get_db)):
    user_stmt = select(User).where(User.id == Emi_request.user_id)
    category_stmt = select(Category).where(Category.id == Emi_request.category_id)
    payment_stmt = select(PaymentMethod).where(PaymentMethod.id == Emi_request.payment_method_id)

    exist_user = db.execute(user_stmt).scalar_one_or_none()
    exist_category = db.execute(category_stmt).scalar_one_or_none()
    exist_payment = db.execute(payment_stmt).scalar_one_or_none()

    if exist_user is None or exist_category is None or exist_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    if exist_category.type != "emi":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This category is not valid for emis"
        )
    emi_data = Emi_request.model_dump()
    emi_data["installments_paid"] = 0
    emi_data["installments_remaining"] = Emi_request.emi_months

    emis = EMI(**emi_data)
    db.add(emis)
    db.commit()
    db.refresh(emis)
    return emis


@router.get("/", response_model=List[EMIOut])
def get_emis(db: Session = Depends(get_db)):
    emi = select(EMI)
    result = db.execute(emi)
    return result.scalars().all()


@router.get("/{emi_id}", response_model=EMIOut)
def get_emi(emi_id: int, db: Session = Depends(get_db)):
    emi = select(EMI).where(EMI.id == emi_id)
    search = db.execute(emi).scalar_one_or_none()
    if search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "EMI not found")
    return search

@router.put("/{emi_id}", response_model=EMIOut)
def update_emi(emi_id: int, emi_reqest: EMIUpdate, db: Session = Depends(get_db)):
    emi=select(EMI).where(EMI.id == emi_id)
    update = db.execute(emi).scalar_one_or_none()
    if update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EMI not found")
    update.item_name = emi_reqest.item_name
    update.total_amount = emi_reqest.total_amount
    update.emi_months = emi_reqest.emi_months
    update.monthly_installment = emi_reqest.monthly_installment
    update.start_date = emi_reqest.start_date
    update.next_due_date = emi_reqest.next_due_date
    update.installments_paid = emi_reqest.installments_paid
    update.installments_remaining = emi_reqest.installments_remaining
    update.status = emi_reqest.status

    db.commit()
    db.refresh(update)
    return update

@router.delete("/{emi_id}")
def delete_emi(emi_id : int, db: Session = Depends(get_db)):
    emi = select(EMI).where(EMI.id == emi_id)
    dele = db.execute(emi).scalar_one_or_none()
    if dele is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "EMI not found" )
    db.delete(dele)
    db.commit()
    return{
        "message":"EMI has been Deleted successfuly"
    }
