from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse
from typing import Optional

class GetBookByIdUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int) -> Optional[BookResponse]:
        book = self.book_repository.get_by_id(book_id)
        return BookResponse.model_validate(book) if book else None
