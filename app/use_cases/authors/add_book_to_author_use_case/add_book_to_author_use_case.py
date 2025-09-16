from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from typing import Optional
from dtos.author_dto import AuthorResponse 


class AddBookToAuthorUseCase:
    def __init__(self, author_repository: AuthorRepository, book_repository: BookRepository):
        self.author_repository = author_repository
        self.book_repository = book_repository

    def execute(self, author_id: int, book_id: int) -> Optional[AuthorResponse]:
        author = self.author_repository.get_by_id(author_id)
        book = self.book_repository.get_by_id(book_id)
        
        if not author or not book:
            return None

        if book not in author.books:
            author.books.append(book)
            self.author_repository.update(author)

        return AuthorResponse.model_validate(author)

