from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserBasic(BaseModel):
    name : str = Field(
        min_length=2,
        max_length=100
        )
    
    email : EmailStr

    phone : str = Field(
        min_length=8,
        max_length=15
        )
class UserCreate(UserBasic):
    password : str = Field(
        min_length=5,
        max_length=100
    )

class UserOut(UserBasic):
    id : int
    created_at : datetime
    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    type: str = Field(min_length=2, max_length=50)

class CategoryOut(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        from_attributes = True