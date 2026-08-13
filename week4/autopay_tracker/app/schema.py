from pydantic import BaseModel, Field, EmailStr
from datetime import date


class UserBasic(BaseModel):
    name : str = Field(min_length=2,max_length=100)
    
    email : EmailStr

    phone : str = Field(min_length=8,max_length=15)


class UserCreate(UserBasic):
    password : str = Field(min_length=5,max_length=100)


class UserOut(UserBasic):
    id : int
    created_at : date
    class Config:
        from_attributes = True

class UserUpdate(UserBasic):
    pass



'''----------------------------------------------------------------------------------------------------------------'''


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)# "OTT", "Recharge", "Electronics"
    type: str = Field(min_length=2, max_length=50)# "subscription" or "emi" 


class CategoryOut(BaseModel):
    id: int
    name: str
    type: str


    class Config:
        from_attributes = True



'''----------------------------------------------------------------------------------------------------------------'''


class PaymentMethodBase(BaseModel):
    type: str = Field(min_length=2, max_length=50)          # "card", "upi", "netbanking", "wallet", "cash"
    provider_name: str = Field(min_length=2, max_length=50)  # "HDFC", "GPay", "ICIC"
    is_default: bool = Field(default=False)


class PaymentMethodCreate(PaymentMethodBase):
    user_id: int   


class PaymentMethodUpdate(PaymentMethodBase):
    pass   

class PaymentMethodOut(PaymentMethodBase):
    id: int
    user_id: int  

    class Config:
        from_attributes = True



'''----------------------------------------------------------------------------------------------------------------'''



class SubscriptionBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    amount: float
    billing_cycle: str = Field(min_length=2)
    start_date: date
    next_due_date: date
    status: str = Field(min_length=2, max_length=30)
    auto_renew: bool = Field(default=False)


class SubscriptionCreate(SubscriptionBase):
    user_id: int
    category_id: int
    payment_method_id: int


class SubscriptionUpdate(SubscriptionBase):
    pass   


class SubscriptionOut(SubscriptionBase):
    id: int
    user_id: int
    category_id: int
    payment_method_id: int

    class Config:
        from_attributes = True

'''..............................................................................'''



class EMIBase(BaseModel):
    item_name: str = Field(min_length=2, max_length=50)   # name of the product purchased
    total_amount: float
    emi_months: int
    monthly_installment: float      # amount to pay each month
    start_date: date
    next_due_date: date
    status: str = Field(min_length=2, max_length=30)      # "active", "completed", "defaulted"


class EMICreate(EMIBase):
    user_id: int
    category_id: int
    payment_method_id: int


class EMIUpdate(EMIBase):
    installments_paid: int
    installments_remaining: int


class EMIOut(EMIBase):
    id: int
    user_id: int
    category_id: int
    payment_method_id: int
    installments_paid: int
    installments_remaining: int

    class Config:
        from_attributes = True


'''--------------------------------------------------------------------------------------------------------------------'''


class PaymentHistoryBase(BaseModel):
    amount_paid : float
    paid_on : date
    status : str = Field(min_length=2, max_length=30)

class PaymentHistoryCreate(PaymentHistoryBase):
    user_id : int
    payment_method_id : int
    subscription_id : int | None = None
    emi_id : int | None = None

class PaymentHistoryOut(PaymentHistoryBase):
    id : int
    user_id : int
    payment_method_id : int
    subscription_id : int | None = None
    emi_id : int | None = None
    class Config:
        from_attributes = True