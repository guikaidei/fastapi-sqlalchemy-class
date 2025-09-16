from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse

class DeleteBookUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int) -> bool:
        book = self.book_repository.get(book_id)
        if not book:
            return None
        response = self.book_repository.delete(book_id)
        return BookResponse.model_validate(response)
