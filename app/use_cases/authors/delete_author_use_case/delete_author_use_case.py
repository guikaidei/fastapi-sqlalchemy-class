from repositories.author_repository import AuthorRepository
from dtos.author_dto import AuthorResponse 


class DeleteAuthorUseCase:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, author_id: int) -> AuthorResponse | None:
        author = self.author_repository.get_by_id(author_id)
        if not author:
            return None
        response = self.author_repository.delete(author_id)
        return AuthorResponse.model_validate(response)
