from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Subscription, User, PaymentMethod, Category
from app.schema import SubscriptionCreate, SubscriptionOut, SubscriptionUpdate
from typing import List



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
    sub = select(Subscription).where(Subscription.id == sub_id)
    search = db.execute(sub).scalar_one_or_none()
    if search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription Method not found")
    return search



@router.put("/{sub_id}", response_model=SubscriptionOut)
def update_subscription(sub_id: int, sub_request: SubscriptionUpdate, db: Session = Depends(get_db)):
    subscrp = select(Subscription).where(Subscription.id == sub_id)
    updat = db.execute(subscrp).scalar_one_or_none()

    if updat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found")

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
    sub = select(Subscription).where(Subscription.id == sub_id)
    dele = db.execute(sub).scalar_one_or_none()
    if dele is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(dele)
    db.commit()

    return{
        "message":"Subscription has been deleted"
    }