from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Subscription, User, Category, PaymentMethod
from app.schema import SubscriptionCreate, SubscriptionUpdate
from app.utility import require_exists
from app.crud import subscription_crud

def create_subscription(db: Session, request: SubscriptionCreate):
    require_exists(db, User, request.user_id, "User")
    category = require_exists(db, Category, request.category_id, "Category")
    require_exists(db, PaymentMethod, request.payment_method_id, "Payment Method")

    if category.type != "subscription":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This category is not valid for subscriptions")

    subscription = Subscription(**request.model_dump())
    return subscription_crud.create(db, subscription)

def get_subscription(db: Session, sub_id: int):
    return require_exists(db, Subscription, sub_id, "Subscription")

def list_subscriptions(db: Session):
    return subscription_crud.get_all(db)

def update_subscription(db: Session, sub_id: int, request: SubscriptionUpdate):
    subscription = require_exists(db, Subscription, sub_id, "Subscription")
    subscription.name = request.name
    subscription.amount = request.amount
    subscription.billing_cycle = request.billing_cycle
    subscription.start_date = request.start_date
    subscription.next_due_date = request.next_due_date
    subscription.status = request.status
    subscription.auto_renew = request.auto_renew
    return subscription_crud.update(db, subscription)

def delete_subscription(db: Session, sub_id: int):
    subscription = require_exists(db, Subscription, sub_id, "Subscription")
    subscription_crud.delete(db, subscription)