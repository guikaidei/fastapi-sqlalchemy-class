from repositories.book_repository import BookRepository
from dtos.book_dto import BookResponse

class GetAllBooksUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self) -> list[BookResponse]:
        books = self.book_repository.get_all()
        return [BookResponse.model_validate(book) for book in books]
