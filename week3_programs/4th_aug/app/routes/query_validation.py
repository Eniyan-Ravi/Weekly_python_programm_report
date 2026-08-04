#query_validation
from fastapi import APIRouter, Query
from app.database import BOOKS

router = APIRouter(
    tags=["Query Validation"]
)


@router.get("/books")
async def search_books(

    rating: float = Query(
        ge=1,
        le=5,
        description="Minimum Rating"
    )

):

    result = []

    for book in BOOKS:

        if book["rating"] >= rating:
            result.append(book)

    return result