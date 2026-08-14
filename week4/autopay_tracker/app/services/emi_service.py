from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import EMI, User, Category, PaymentMethod
from app.schema import EMICreate, EMIUpdate
from app.utility import require_exists
from app.crud import emi_crud

def create_emi(db: Session, request: EMICreate):
    require_exists(db, User, request.user_id, "User")
    category = require_exists(db, Category, request.category_id, "Category")
    require_exists(db, PaymentMethod, request.payment_method_id, "Payment Method")

    if category.type != "emi":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This category is not valid for emis")

    emi_data = request.model_dump()
    emi_data["installments_paid"] = 0
    emi_data["installments_remaining"] = request.emi_months

    emi = EMI(**emi_data)
    return emi_crud.create(db, emi)

def get_emi(db: Session, emi_id: int):
    return require_exists(db, EMI, emi_id, "EMI")

def list_emis(db: Session):
    return emi_crud.get_all(db)

def update_emi(db: Session, emi_id: int, request: EMIUpdate):
    emi = require_exists(db, EMI, emi_id, "EMI")
    emi.item_name = request.item_name
    emi.total_amount = request.total_amount
    emi.emi_months = request.emi_months
    emi.monthly_installment = request.monthly_installment
    emi.start_date = request.start_date
    emi.next_due_date = request.next_due_date
    emi.installments_paid = request.installments_paid
    emi.installments_remaining = request.installments_remaining
    emi.status = request.status
    return emi_crud.update(db, emi)

def delete_emi(db: Session, emi_id: int):
    emi = require_exists(db, EMI, emi_id, "EMI")
    emi_crud.delete(db, emi)