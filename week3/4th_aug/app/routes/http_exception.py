#http_exception.py
from fastapi import APIRouter, HTTPException
from app.database import BOOKS

router = APIRouter(
    tags=["HTTP Exception"]
)


@router.get("/books/{book_id}")
async def get_book(book_id: int):

    for book in BOOKS:

        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )