from pydantic import BaseModel, Field


class CustomerRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: str = Field(
        min_length=5,
        max_length=150
    )

    age: int = Field(
        ge=13,
        le=100
    )


class ReviewRequest(BaseModel):

    game_name: str = Field(
        min_length=2,
        max_length=100
    )

    customer_id: int = Field(
        gt=0
    )

    rating: int = Field(
        ge=1,
        le=5
    )

    review: str = Field(
        min_length=5,
        max_length=500
    )

    price: float = Field(
        ge=0
    )