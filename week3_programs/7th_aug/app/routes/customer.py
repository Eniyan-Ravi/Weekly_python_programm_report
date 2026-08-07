from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Customer
from app.schema import CustomerRequest


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create_customer(customer_request: CustomerRequest,db: Session = Depends(get_db)):

    stmt = select(Customer).where(Customer.email == customer_request.email)

    existing_customer = db.execute(stmt).scalar_one_or_none()

    if existing_customer:
        raise HTTPException(status_code=400,detail="Email already registered")

    customer = Customer(**customer_request.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    stmt = select(Customer)
    result = db.execute(stmt)
    return result.scalars().all()

@router.get("/{customer_id}")
def get_customer(customer_id: int,db: Session = Depends(get_db)):

    stmt = select(Customer).where(Customer.id == customer_id)

    customer = db.execute(stmt).scalar_one_or_none()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put("/{customer_id}")
def update_customer(customer_id: int,customer_request: CustomerRequest,db: Session = Depends(get_db)):

    stmt = select(Customer).where(Customer.id == customer_id)

    customer = db.execute(stmt).scalar_one_or_none()

    if customer is None:
        raise HTTPException(status_code=404,detail="Customer not found")
    customer.name = customer_request.name
    customer.email = customer_request.email
    customer.age = customer_request.age
    db.commit()
    db.refresh(customer)
    return customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int,db: Session = Depends(get_db)):

    stmt = select(Customer).where(Customer.id == customer_id)
    customer = db.execute(stmt).scalar_one_or_none()

    if customer is None:
        raise HTTPException(status_code=404,detail="Customer not found")
    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }