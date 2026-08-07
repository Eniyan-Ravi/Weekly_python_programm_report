from sqlalchemy import String, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True
    )

    age: Mapped[int] = mapped_column(
        Integer
    )


class GameReview(Base):

    __tablename__ = "game_reviews"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    game_name: Mapped[str] = mapped_column(
        String(100)
    )

    customer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("customers.id")
    )

    rating: Mapped[int] = mapped_column(
        Integer
    )

    review: Mapped[str] = mapped_column(
        Text
    )

    price: Mapped[float] = mapped_column(
        Float
    )