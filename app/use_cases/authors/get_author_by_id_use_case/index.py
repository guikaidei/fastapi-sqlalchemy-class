from fastapi import APIRouter, Depends, HTTPException
from repositories.author_repository import AuthorRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.author_dto import AuthorResponse 
from use_cases.authors.get_author_by_id_use_case.get_author_by_id_use_case import GetAuthorByIdUseCase

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> GetAuthorByIdUseCase:
    author_repository = AuthorRepository(db)
    return GetAuthorByIdUseCase(author_repository)

@router.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author_by_id(author_id: int, use_case: GetAuthorByIdUseCase = Depends(get_use_case)):
    author = use_case.execute(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
