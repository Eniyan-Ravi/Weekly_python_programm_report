from sqlalchemy import String, DateTime, Boolean, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    password: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))



class Category(Base):
    __tablename__ = "category"
    id : Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String(150))
    type : Mapped[str] = mapped_column(String(150))



class PaymentMethod(Base):
    __tablename__ = "paymentmethod"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    type : Mapped[str] = mapped_column(String(50))
    provider_name : Mapped[str] = mapped_column(String(50))
    is_default : Mapped[bool] = mapped_column(Boolean, default=False)


class Subscription(Base):
    __tablename__ = "subscription"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id : Mapped[int] = mapped_column(ForeignKey("category.id"))
    payment_method_id : Mapped[int] = mapped_column(ForeignKey("paymentmethod.id"))
    name : Mapped[str] = mapped_column(String(40))
    amount : Mapped[float] = mapped_column(Float, nullable=False)
    billing_cycle : Mapped[str] = mapped_column(String(20))
    start_date : Mapped[datetime] = mapped_column(DateTime)
    next_due_date : Mapped[datetime] = mapped_column(DateTime)
    status : Mapped[str] = mapped_column(String(20),nullable=False)
    auto_renew : Mapped[bool] = mapped_column(Boolean, default=False)


class EMI(Base):
    __tablename__ = "emi"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id : Mapped[int] = mapped_column(ForeignKey("category.id"))
    payment_method_id : Mapped[int] = mapped_column(ForeignKey("paymentmethod.id"))
    item_name : Mapped[str] = mapped_column(String(50), nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    emi_months : Mapped[int] = mapped_column(Integer)
    monthly_installment : Mapped[float] = mapped_column(Float)
    start_date : Mapped[datetime] = mapped_column(DateTime)
    next_due_date : Mapped[datetime] = mapped_column(DateTime)
    installments_paid : Mapped[float] = mapped_column(Float,default=0)
    installments_remaining : Mapped[int] = mapped_column(Integer)
    status : Mapped[str] = mapped_column(String(30))
