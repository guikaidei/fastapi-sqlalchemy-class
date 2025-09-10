from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Author(BaseModel):
    """
    Entidade Author usando Pydantic
    Representa um autor no domínio da aplicação
    """
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    books: List['Book'] = Field(default_factory=list)

    class Config:
        # Permite conversão de objetos SQLAlchemy
        from_attributes = True

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

# Resolve forward references
from .book import Book
Author.model_rebuild()