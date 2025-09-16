from fastapi import APIRouter, Depends, HTTPException
from repositories.author_repository import AuthorRepository
from database.database import get_db
from sqlalchemy.orm import Session
from dtos.author_dto import AuthorResponse 
from use_cases.authors.update_author_use_case.update_author_use_case import UpdateAuthorUseCase
from dtos.author_dto import UpdateAuthorRequest

router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> UpdateAuthorUseCase:
    author_repository = AuthorRepository(db)
    return UpdateAuthorUseCase(author_repository)

@router.put("/authors/{author_id}", response_model= AuthorResponse)
def update_author(author_id: int, request: UpdateAuthorRequest, use_case: UpdateAuthorUseCase = Depends(get_use_case)):
    author = use_case.execute(author_id, request.name, request.email)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
