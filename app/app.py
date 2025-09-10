from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from repositories.author_repository import AuthorRepository
from entities.author import Author
from models.author_model import AuthorModel

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/authors/", response_model=Author)
def create_author(author: Author, db: Session = Depends(get_db)):
    repo = AuthorRepository(db)
    # Lógica de criação
    author_model = AuthorModel(name=author.name, email=author.email)
    created_author = repo.add(author_model)
    return created_author