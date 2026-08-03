from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI(
    title="Book Management API"
)


class Book:
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "rating": self.rating
        }
class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [
    Book(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "A boy discovers he is a wizard.", 4.9),
    Book(2, "Goosebumps: Night of the Living Dummy", "R.L. Stine", "A haunted dummy causes trouble.", 4.7),
    Book(3, "Percy Jackson and the Lightning Thief", "Rick Riordan", "A demigod begins a dangerous quest.", 4.8),
    Book(4, "The Chronicles of Narnia", "C.S. Lewis", "Children enter a magical world.", 4.8),
    Book(5, "Coraline", "Neil Gaiman", "A girl finds a creepy hidden world.", 4.7)
]



@app.get("/books")
async def read_all_books():
    return [book.to_dict() for book in BOOKS]

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)  

def find_book_id(book: Book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id + 1 
    else:
        book.id=1
    return book