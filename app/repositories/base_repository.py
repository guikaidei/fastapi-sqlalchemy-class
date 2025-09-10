from sqlalchemy.orm import Session
from typing import TypeVar, Type, Generic

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def get_all(self) -> list[T]:
        return self.session.query(self.model).all()

    def get_by_id(self, id: int) -> T | None:
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, id: int):
        entity = self.get_by_id(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()