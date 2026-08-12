from sqlalchemy import String, Date, Boolean, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date,datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    password: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[date] = mapped_column(Date, default=lambda: datetime.now(timezone.utc).date())


class Category(Base):
    __tablename__ = "category"
    id : Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String(150))# "OTT", "Recharge", "Electronics"
    type : Mapped[str] = mapped_column(String(150))# "subscription" or "emi"



class PaymentMethod(Base):
    __tablename__ = "paymentmethod"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    type : Mapped[str] = mapped_column(String(50))# "card", "upi", "netbanking", "wallet", "cash"
    provider_name : Mapped[str] = mapped_column(String(50))#"HDFC", "GPay", "ICIC"
    is_default : Mapped[bool] = mapped_column(Boolean, default=False)


class Subscription(Base):
    __tablename__ = "subscription"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id : Mapped[int] = mapped_column(ForeignKey("category.id"))
    payment_method_id : Mapped[int] = mapped_column(ForeignKey("paymentmethod.id"))
    name : Mapped[str] = mapped_column(String(40))# "Netflix", "Jio ", "Airtel Wifi"
    amount : Mapped[float] = mapped_column(Float, nullable=False)# recurring charge amount
    billing_cycle : Mapped[str] = mapped_column(String(20)) #"monthly", "yearly", "weekly"
    start_date : Mapped[datetime] = mapped_column(Date)
    next_due_date : Mapped[datetime] = mapped_column(Date)
    status : Mapped[str] = mapped_column(String(20),nullable=False)# "active", "paused", "cancelled"
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
    start_date : Mapped[datetime] = mapped_column(Date)
    next_due_date : Mapped[datetime] = mapped_column(Date)
    installments_paid : Mapped[int] = mapped_column(Integer,default=0)
    installments_remaining : Mapped[int] = mapped_column(Integer)
    status : Mapped[str] = mapped_column(String(30))



class PaymentHistory(Base):
    __tablename__ = "payment_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("paymentmethod.id"))
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscription.id"), nullable=True)
    emi_id: Mapped[int] = mapped_column(ForeignKey("emi.id"), nullable=True)
    amount_paid: Mapped[float] = mapped_column(Float, nullable=False)
    paid_on: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)