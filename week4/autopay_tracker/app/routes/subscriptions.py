from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Subscription, User, PaymentMethod, Category
from app.schema import SubscriptionCreate, SubscriptionOut, SubscriptionUpdate
from typing import List
from app.utility import require_exists



router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])


@router.post("/", response_model=SubscriptionOut)
def create_subscription(sub_request: SubscriptionCreate, db: Session = Depends(get_db)):
    user_stmt = select(User).where(User.id == sub_request.user_id)
    category_stmt = select(Category).where(Category.id == sub_request.category_id)
    payment_stmt = select(PaymentMethod).where(PaymentMethod.id == sub_request.payment_method_id)

    exist_user = db.execute(user_stmt).scalar_one_or_none()
    exist_category = db.execute(category_stmt).scalar_one_or_none()
    exist_payment = db.execute(payment_stmt).scalar_one_or_none()

    if exist_user is None or exist_category is None or exist_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    if exist_category.type !="subscription":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This category is not valid for subscriptions"
        )
    subscriptions = Subscription(**sub_request.model_dump())
    db.add(subscriptions)
    db.commit()
    db.refresh(subscriptions)
    return subscriptions



@router.get("/", response_model=List[SubscriptionOut])
def get_subscriptions(db: Session = Depends(get_db)):
    sub = select(Subscription)
    result = db.execute(sub)
    return result.scalars().all()


@router.get("/{sub_id}", response_model=SubscriptionOut)
def get_subscription(sub_id: int, db: Session = Depends(get_db)):
    return require_exists(db, Subscription, sub_id, "Subscription")



@router.put("/{sub_id}", response_model=SubscriptionOut)
def update_subscription(sub_id: int, sub_request: SubscriptionUpdate, db: Session = Depends(get_db)):
    updat = require_exists(db, Subscription, sub_id, "Subscription")

    updat.name = sub_request.name
    updat.amount = sub_request.amount
    updat.billing_cycle = sub_request.billing_cycle
    updat.start_date = sub_request.start_date
    updat.next_due_date = sub_request.next_due_date
    updat.status = sub_request.status
    updat.auto_renew = sub_request.auto_renew

    db.commit()
    db.refresh(updat)
    return updat


@router.delete("/{sub_id}")
def delete_subscription(sub_id: int, db:Session = Depends(get_db)):
    dele = require_exists(db, Subscription, sub_id, "Subscription")

    db.delete(dele)
    db.commit()

    return{
        "message":"Subscription has been deleted"
    }