from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class BookModel(Base):
    __tablename__ = "books"  # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)  # Chave primária
    title = Column(String, index=True)                   # Título do livro
    isbn = Column(String, unique=True, index=True)       # ISBN único

    # Relacionamento many-to-many com autores
    authors = relationship(
        "AuthorModel",                      # Classe relacionada
        secondary="author_book_association", # Tabela de associação
        back_populates="books"          # Relacionamento reverso
    )

    def __repr__(self):
        return f"<BookModel(id={self.id}, title='{self.title}', isbn='{self.isbn}')>"