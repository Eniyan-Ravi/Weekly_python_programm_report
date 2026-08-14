from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import PaymentHistory, User, PaymentMethod, Subscription, EMI
from app.schema import PaymentHistoryCreate
from app.utility import require_exists
from app.crud import payment_history_crud

def create_payment_history(db: Session, request: PaymentHistoryCreate):
    require_exists(db, User, request.user_id, "User")
    require_exists(db, PaymentMethod, request.payment_method_id, "Payment Method")

    if (request.subscription_id is None) == (request.emi_id is None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Exactly one of subscription_id or emi_id must be provided"
        )

    if request.subscription_id is not None:
        require_exists(db, Subscription, request.subscription_id, "Subscription")

    if request.emi_id is not None:
        require_exists(db, EMI, request.emi_id, "EMI")

    payhistory = PaymentHistory(**request.model_dump())
    return payment_history_crud.create(db, payhistory)

def get_payment_history(db: Session, payhistory_id: int):
    return require_exists(db, PaymentHistory, payhistory_id, "Payment History")

def list_payment_histories(db: Session):
    return payment_history_crud.get_all(db)