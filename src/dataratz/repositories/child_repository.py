from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID
from dataratz.domain.child import Child
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import MappedColumn
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session

from dataratz.repositories.db_config import Base


class ChildRepository:    
    async def add(self, child: Child) -> None:
        raise NotImplementedError
    async def get(self, id: UUID) -> Child | None:
        raise NotImplementedError
    

class ChildInMemoryRepository(ChildRepository):
    children: dict[UUID, Child] = dict()

    async def add(self, child: Child) -> None:
        self.children[child.id] = child

    async def get(self, id: UUID) -> Child | None:
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

@dataclass
class ChildDBRepository(ChildRepository):
    session: Session

    async def add(self, child: Child) -> None:
        self.session.add(child)

    async def get(self, id: UUID) -> Child | None:
        result = self.session.query(ChildDB).filter_by(id=id).one_or_none()
        if result:
            return result.to_domain()
        else:
            return None
