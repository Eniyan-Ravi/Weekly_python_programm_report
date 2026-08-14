from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import SubscriptionCreate, SubscriptionOut, SubscriptionUpdate
from app.services import subscription_service

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/", response_model=SubscriptionOut)
def create_subscription(sub_request: SubscriptionCreate, db: Session = Depends(get_db)):
    return subscription_service.create_subscription(db, sub_request)

@router.get("/", response_model=List[SubscriptionOut])
def get_subscriptions(db: Session = Depends(get_db)):
    return subscription_service.list_subscriptions(db)

@router.get("/{sub_id}", response_model=SubscriptionOut)
def get_subscription(sub_id: int, db: Session = Depends(get_db)):
    return subscription_service.get_subscription(db, sub_id)

@router.put("/{sub_id}", response_model=SubscriptionOut)
def update_subscription(sub_id: int, sub_request: SubscriptionUpdate, db: Session = Depends(get_db)):
    return subscription_service.update_subscription(db, sub_id, sub_request)

@router.delete("/{sub_id}")
def delete_subscription(sub_id: int, db: Session = Depends(get_db)):
    subscription_service.delete_subscription(db, sub_id)
    return {"message": "Subscription has been deleted"}