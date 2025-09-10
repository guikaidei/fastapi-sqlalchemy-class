from database.database import SessionLocal, Base, engine
from models.author_model import AuthorModel
from models.book_model import BookModel
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from entities.author import Author
from entities.book import Book 

def main():
    session = SessionLocal()

    try:
        author_repo = AuthorRepository(session)
        book_repo = BookRepository(session)
        author_book_association = Base.metadata.tables.get("author_book_association")
        
        # Limpar dados existentes para o exemplo
        session.query(AuthorModel).delete()
        session.query(BookModel).delete()
        session.query(author_book_association).delete()
        session.commit()

        # Criar autores usando entidades para validação
        authors_data = [
            {"name": "Clarice Lispector", "email": "clarice@email.com"},
            {"name": "Jorge Amado", "email": "jorge@email.com"},
            {"name": "Paulo Coelho", "email": "paulo@email.com"}
        ]

        authors = []
        for data in authors_data:
            # Usar entidade para validação
            author_entity = Author(**data)
            # Converter para modelo
            author_model = AuthorModel(name=author_entity.name, email=author_entity.email)
            author = author_repo.add(author_model)
            authors.append(author)
            print(f"Autor criado: {author.name}")

        # Criar livros usando entidades para validação
        books_data = [
            {"title": "A Hora da Estrela", "isbn": "978-8520925829"},
            {"title": "Gabriela, Cravo e Canela", "isbn": "978-8535902976"},
            {"title": "O Alquimista", "isbn": "978-8595081413"},
            {"title": "Água Viva", "isbn": "978-8520925836"}
        ]

        books = []
        for data in books_data:
            # Usar entidade para validação
            book_entity = Book(**data)
            # Converter para modelo
            book_model = BookModel(title=book_entity.title, isbn=book_entity.isbn)
            book = book_repo.add(book_model)
            books.append(book)
            print(f"Livro criado: {book.title}")

        # Estabelecer relacionamentos
        # Clarice Lispector - A Hora da Estrela e Água Viva
        books[0].authors.append(authors[0])  # A Hora da Estrela
        books[3].authors.append(authors[0])  # Água Viva

        # Jorge Amado - Gabriela, Cravo e Canela
        books[1].authors.append(authors[1])

        # Paulo Coelho - O Alquimista
        books[2].authors.append(authors[2])

        session.commit()

        # Demonstrar buscas
        print("\n=== BUSCAS ===")

        # Autores com livros
        authors_with_books = author_repo.get_authors_with_books()
        print(f"Autores com livros: {len(authors_with_books)}")

        # Busca por nome parcial
        clarice_authors = author_repo.get_by_name("Clarice")
        print(f"Autores com 'Clarice': {[a.name for a in clarice_authors]}")

        # Livros de um autor específico
        clarice = author_repo.get_by_email("clarice@email.com")
        print(f"Livros da Clarice: {[book.title for book in clarice.books]}")

        # Update - Alterar email de um autor usando entidade para validação
        paulo = author_repo.get_by_email("paulo@email.com")
        # Validar com entidade
        updated_entity = Author(name=paulo.name, email="paulo.coelho@email.com")
        paulo.email = updated_entity.email
        updated_paulo = author_repo.update(paulo)
        print(f"Email atualizado: {updated_paulo.email}")

        # Delete - Remover um livro
        book_to_delete = book_repo.get_by_isbn("978-8520925836")
        if book_to_delete:
            book_repo.delete(book_to_delete.id)
            print(f"Livro '{book_to_delete.title}' removido")

    finally:
        session.close()

if __name__ == "__main__":
    main()