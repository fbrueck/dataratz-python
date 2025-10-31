from dataclasses import dataclass
from uuid import UUID

from dataratz.domain.child import Child
from dataratz.repositories.child_repository import ChildRepository


@dataclass
class ChildCreate:
    child_repsoitory: ChildRepository

    async def create_child(self, child: Child) -> None:
        await self.child_repsoitory.add(child)


@dataclass
class ChildGet:
    child_repsoitory: ChildRepository

    async def get_child(self, id: UUID) -> Child | None:
        return await self.child_repsoitory.get(id)
