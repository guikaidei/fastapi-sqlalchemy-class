from sqlalchemy.orm import Session
from models.author_model import AuthorModel
from repositories.base_repository import BaseRepository

class AuthorRepository(BaseRepository[AuthorModel]):
    def __init__(self, session: Session):
        super().__init__(session, AuthorModel)

    def get_by_email(self, email: str) -> AuthorModel | None:
        """Busca um autor pelo email"""
        return self.session.query(AuthorModel).filter(AuthorModel.email == email).first()

    def get_by_name(self, name: str) -> list[AuthorModel]:
        """Busca autores pelo nome (busca parcial)"""
        return self.session.query(AuthorModel).filter(AuthorModel.name.ilike(f"%{name}%")).all()

    def get_authors_with_books(self) -> list[AuthorModel]:
        """Retorna autores que têm livros"""
        return self.session.query(AuthorModel).join(AuthorModel.books).distinct().all()