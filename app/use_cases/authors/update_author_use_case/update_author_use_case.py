from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse 
from typing import Optional

class UpdateAuthorUseCase:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, author_id: int, name: str, email: str) -> Optional[AuthorResponse]:
        author = self.author_repository.get_by_id(author_id)
        if not author:
            return None
        
        author.name = name
        author.email = email
        updated_author = self.author_repository.update(author)
        return AuthorResponse.model_validate(updated_author)
