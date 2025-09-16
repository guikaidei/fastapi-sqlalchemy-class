from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse 
from typing import Optional

class GetAuthorByIdUseCase:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, author_id: int) -> Optional[AuthorResponse]:
        author = self.author_repository.get_by_id(author_id)
        return AuthorResponse.model_validate(author)
