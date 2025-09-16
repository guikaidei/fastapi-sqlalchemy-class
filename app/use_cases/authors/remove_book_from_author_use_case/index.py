from fastapi import APIRouter, Depends, HTTPException
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.author_dto import AuthorResponse 
from use_cases.authors.remove_book_from_author_use_case.remove_book_from_author_use_case import RemoveBookFromAuthorUseCase

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> RemoveBookFromAuthorUseCase:
    author_repository = AuthorRepository(db)
    book_repository = BookRepository(db)
    return RemoveBookFromAuthorUseCase(author_repository, book_repository)

@router.delete("/authors/{author_id}/books/{book_id}", response_model=AuthorResponse)
def remove_book_from_author(author_id: int, book_id: int, use_case: RemoveBookFromAuthorUseCase = Depends(get_use_case)):
    author = use_case.execute(author_id, book_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author or Book not found")
    return author
