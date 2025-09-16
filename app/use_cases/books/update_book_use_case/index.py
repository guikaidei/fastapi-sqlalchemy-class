from fastapi import APIRouter, Depends, HTTPException
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.book_dto import BookResponse
from use_cases.books.update_book_use_case.update_book_use_case import UpdateBookUseCase
from dtos.book_dto import UpdateBookRequest

router = APIRouter()


def get_use_case(db: Session = Depends(get_db)) -> UpdateBookUseCase:
    book_repository = BookRepository(db)
    return UpdateBookUseCase(book_repository)

@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, request: UpdateBookRequest, use_case: UpdateBookUseCase = Depends(get_use_case)):
    book = use_case.execute(book_id, request.title, request.isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
