from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from models.book_model import BookModel
from typing import Optional

class CreateBookUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, title: str, isbn: str) -> BookResponse:
        book_model = BookModel(title=title,  isbn=isbn)
        created_book = self.book_repository.add(book_model)
        return BookResponse.model_validate(created_book)
