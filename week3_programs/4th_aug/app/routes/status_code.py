#status_code
from fastapi import APIRouter, HTTPException, status
from app.database import BOOKS

router = APIRouter(
    tags=["Status Code Practice"]
)


@router.post(
    "/books",
    status_code=status.HTTP_201_CREATED
)
async def create_book(book: dict):

    # Check whether the ID already exists
    for existing_book in BOOKS:
        if existing_book["id"] == book["id"]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Book ID already exists"
            )

    BOOKS.append(book)

    return {
        "message": "Book created successfully",
        "book": book
    }


@router.get(
    "/books/{book_id}",
    status_code=status.HTTP_200_OK
)
async def get_book(book_id: int):

    for book in BOOKS:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@router.delete(
    "/books/{book_id}",
    status_code=status.HTTP_200_OK
)
async def delete_book(book_id: int):

    for book in BOOKS:

        if book["id"] == book_id:

            BOOKS.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )