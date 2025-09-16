from fastapi import APIRouter, Depends, HTTPException
from repositories.author_repository import AuthorRepository
from database.database import get_db
from sqlalchemy.orm import Session
from use_cases.authors.delete_author_use_case.delete_author_use_case import DeleteAuthorUseCase
from dtos.author_dto import AuthorResponse 


router = APIRouter()

def get_use_case(db: Session = Depends(get_db)) -> DeleteAuthorUseCase:
    author_repository = AuthorRepository(db)
    return DeleteAuthorUseCase(author_repository)

@router.delete("/authors/{author_id}")
def delete_author(author_id: int, use_case: DeleteAuthorUseCase = Depends(get_use_case), response_model=AuthorResponse): 
    success = use_case.execute(author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}
