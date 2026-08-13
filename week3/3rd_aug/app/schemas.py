#schemas
from pydantic import BaseModel, Field


class GameRequest(BaseModel):

    id: int | None = None

    name: str = Field(min_length=2, max_length=40)

    genre: str = Field(min_length=3)

    developer: str = Field(min_length=2)

    description: str = Field(min_length=5, max_length=100)

    rating: float = Field(gt=0, le=5)

    price: int = Field(gt=0)