from pydantic import BaseModel, Field
from typing import List, Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=255)
    isbn: Optional[str] = Field(..., min_length=10, max_length=17)
    authors: List['Author'] = Field(default_factory=list)
    
    class Config:
        from_attributes = True
        
    def __str__(self):
        return f"Book: {self.title} ({self.isbn})"
    
# Resolve forward references
from .author import Author
Book.model_rebuild()