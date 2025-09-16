from fastapi import APIRouter, Depends, HTTPException
from repositories.book_repository import BookRepository
from database.database import get_db
from sqlalchemy.orm import Session
from use_cases.books.delete_book_use_case.delete_book_use_case import DeleteBookUseCase

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> DeleteBookUseCase:
    book_repository = BookRepository(db)
    return DeleteBookUseCase(book_repository)

@router.delete("/books/{book_id}")
def delete_book(book_id: int, use_case: DeleteBookUseCase = Depends(get_use_case)):
    success = use_case.execute(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
