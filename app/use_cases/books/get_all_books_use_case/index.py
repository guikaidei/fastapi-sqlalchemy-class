from fastapi import APIRouter, Depends
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.book_dto import BookResponse
from use_cases.books.get_all_books_use_case.get_all_books_use_case import GetAllBooksUseCase

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> GetAllBooksUseCase:
    book_repository = BookRepository(db)
    return GetAllBooksUseCase(book_repository)

@router.get("/books", response_model=list[BookResponse])
def get_all_books(use_case: GetAllBooksUseCase = Depends(get_use_case)):
    return use_case.execute()
