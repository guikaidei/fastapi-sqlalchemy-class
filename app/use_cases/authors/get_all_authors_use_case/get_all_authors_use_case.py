from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse 

class GetAllAuthorsUseCase:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self) -> list[AuthorResponse]:
        authors = self.author_repository.get_all() 
        return [AuthorResponse.model_validate(author) for author in authors]
