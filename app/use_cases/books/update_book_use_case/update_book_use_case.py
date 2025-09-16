from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from typing import Optional

class UpdateBookUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int, title: str, isbn: str) -> Optional[BookResponse]:
        book = self.book_repository.get_by_id(book_id)
        if not book:
            return None
        
        book.title = title
        book.isbn = isbn
        updated_book = self.book_repository.update(book)
        return BookResponse.model_validate(updated_book) if updated_book else None
