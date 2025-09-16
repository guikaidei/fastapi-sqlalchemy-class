from pydantic import BaseModel, EmailStr, Field
from typing import List

class CreateAuthorRequest(BaseModel):
    """
    DTO para requisição de criação de autor
    Contém os dados necessários para criar um novo autor
    """
    name: str = Field(..., min_length=1, max_length=255, description="Nome completo do autor", example="João Silva")
    email: EmailStr = Field(..., description="Email válido do autor", example="joao.silva@example.com")

class UpdateAuthorRequest(BaseModel):
    """
    DTO para requisição de atualização de autor
    Contém os dados que podem ser atualizados de um autor
    """
    name: str = Field(..., min_length=1, max_length=255, description="Nome completo do autor", example="João Silva")
    email: EmailStr = Field(..., description="Email válido do autor", example="joao.silva@example.com")

class BookSummary(BaseModel):
    """
    DTO com resumo das informações de um livro
    Usado para evitar referências circulares na resposta de autores
    """
    id: int = Field(..., description="ID único do livro", example=1)
    title: str = Field(..., description="Título do livro", example="Clean Code")
    isbn: str = Field(..., description="ISBN do livro", example="978-0132350884")

    class Config:
        from_attributes = True

class AuthorResponse(BaseModel):
    """
    DTO de resposta para operações com autores
    Contém todas as informações do autor incluindo seus livros
    """
    id: int = Field(..., description="ID único do autor", example=1)
    name: str = Field(..., description="Nome completo do autor", example="João Silva")
    email: str = Field(..., description="Email do autor", example="joao.silva@example.com")
    books: List[BookSummary] = Field(default_factory=list, description="Lista de livros escritos pelo autor")

    class Config:
        from_attributes = True