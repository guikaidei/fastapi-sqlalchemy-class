from fastapi import APIRouter, Depends
from repositories.author_repository import AuthorRepository
from database.database import get_db
from sqlalchemy.orm import Session
from entities.author import Author
from use_cases.authors.create_author_use_case.create_author_use_case import CreateAuthorUseCase
from dtos.author_dto import CreateAuthorRequest
from pathlib import Path


router = APIRouter()



def get_use_case(db: Session = Depends(get_db)) -> CreateAuthorUseCase:
    author_repository = AuthorRepository(db)
    return CreateAuthorUseCase(author_repository)

@router.post("/authors", response_model=Author, description=Path("app/docs/create_author.md").read_text(), summary="Criação de Autor", tags=["Authors"])
def create_author(request: CreateAuthorRequest, use_case: CreateAuthorUseCase = Depends(get_use_case)):
    return use_case.execute(request.name, request.email)