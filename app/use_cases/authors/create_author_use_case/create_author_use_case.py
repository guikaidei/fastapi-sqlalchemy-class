from repositories.author_repository import AuthorRepository
from entities.author import Author
from models.author_model import AuthorModel

class CreateAuthorUseCase:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, name: str, email: str) -> Author:
        author_model = AuthorModel(name=name, email=email)
        
        created_author = self.author_repository.add(author_model)
        return created_author
