from fastapi import APIRouter, Depends
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.book_dto import BookResponse
from use_cases.books.create_book_use_case.create_book_use_case import CreateBookUseCase
from dtos.book_dto import CreateBookRequest

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> CreateBookUseCase:
    book_repository = BookRepository(db)
    return CreateBookUseCase(book_repository)

@router.post("/books", response_model=BookResponse)
def create_book(request: CreateBookRequest, use_case: CreateBookUseCase = Depends(get_use_case)):
    return use_case.execute(request.title, request.isbn)
