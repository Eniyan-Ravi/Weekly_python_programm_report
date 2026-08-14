from sqlalchemy.orm import Session
from app.models import PaymentMethod, User
from app.schema import PaymentMethodCreate, PaymentMethodUpdate
from app.utility import require_exists
from app.crud import payment_method_crud

def create_payment_method(db: Session, request: PaymentMethodCreate):
    require_exists(db, User, request.user_id, "User")
    payment_method = PaymentMethod(**request.model_dump())
    return payment_method_crud.create(db, payment_method)

def get_payment_method(db: Session, pay_method_id: int):
    return require_exists(db, PaymentMethod, pay_method_id, "Payment Method")

def list_payment_methods(db: Session):
    return payment_method_crud.get_all(db)

def update_payment_method(db: Session, pay_method_id: int, request: PaymentMethodUpdate):
    payment_method = require_exists(db, PaymentMethod, pay_method_id, "Payment Method")
    payment_method.type = request.type
    payment_method.provider_name = request.provider_name
    payment_method.is_default = request.is_default
    return payment_method_crud.update(db, payment_method)

def delete_payment_method(db: Session, pay_method_id: int):
    payment_method = require_exists(db, PaymentMethod, pay_method_id, "Payment Method")
    payment_method_crud.delete(db, payment_method)