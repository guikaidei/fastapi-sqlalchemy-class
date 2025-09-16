from fastapi import APIRouter, Depends, HTTPException
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.book_dto import BookResponse
from use_cases.books.get_book_by_id_use_case.get_book_by_id_use_case import GetBookByIdUseCase

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> GetBookByIdUseCase:
    book_repository = BookRepository(db)
    return GetBookByIdUseCase(book_repository)

@router.get("/books/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int, use_case: GetBookByIdUseCase = Depends(get_use_case)):
    book = use_case.execute(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
