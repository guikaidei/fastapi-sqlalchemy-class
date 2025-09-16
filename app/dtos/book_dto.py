from pydantic import BaseModel, EmailStr
from typing import List

class CreateBookRequest(BaseModel):
    title: str
    isbn: str
    
class UpdateBookRequest(BaseModel):
    title: str
    isbn: str
        
class AuthorSummary(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    authors: List[AuthorSummary] = []

    class Config:
        from_attributes = True