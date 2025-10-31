from __future__ import annotations
from uuid import UUID
from dataratz.domain.child import Child
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import MappedColumn
from sqlalchemy.orm import Mapped

from dataratz.repositories.db_config import Base


class ChildRepository:    
    def add(self, child: Child) -> None:
        raise NotImplementedError
    def get(self, id: UUID) -> Child | None:
        raise NotImplementedError
    

class ChildInMemoryRepository(ChildRepository):
    children: dict[UUID, Child] = dict()

    def add(self, child: Child) -> None:
        self.children[child.id] = child

    def get(self, id: UUID) -> Child | None:
        return self.children.get(id, None)


class ChildDB(Base):
    __tablename__ = "children"

    id: Mapped[UUID] = MappedColumn(
        SQLAlchemyUUID(as_uuid=True), primary_key=True, nullable=False
    )
    first_name: Mapped[str] = MappedColumn(String, nullable=False)
    last_name: Mapped[str] = MappedColumn(String, nullable=False)

    def to_domain(self) -> Child:
        return Child(id=self.id, first_name=self.first_name, last_name=self.last_name)

    @staticmethod
    def from_domain(child: Child) -> ChildDB:
        return ChildDB(
            id=child.id, first_name=child.first_name, last_name=child.last_name
        )


class ChildDBRepository(ChildRepository):
    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def add(self, child: Child) -> None:
        with self.session_factory() as session:
            session.add(child)
            session.commit()

    def get(self, id: UUID) -> Child | None:
        with self.session_factory() as session:
            return session.get(Child, id)
