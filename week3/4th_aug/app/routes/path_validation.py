#path_validation
from fastapi import APIRouter, Path
from app.database import BOOKS

router = APIRouter(
    tags=["Path Validation"]
)


@router.get("/book/title/{title}")
async def search_book(

    title: str = Path(
        min_length=3,
        max_length=30,
        description="Enter Book Title"
    )

):

    for book in BOOKS:

        if book["title"].lower() == title.lower():
            return book

    return {"message": "Book not found"}