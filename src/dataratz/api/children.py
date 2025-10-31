from __future__ import annotations

from uuid import UUID
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dataratz.domain.child import Child
from dataratz.repositories.child_repository import ChildInMemoryRepository
from dataratz.use_cases.child_use_cases import (
    ChildCreate,
    ChildGet,
)

children_router = APIRouter(prefix="/children")


class ChildCreateDto(BaseModel):
    first_name: str
    last_name: str

    def to_domain(self) -> Child:
        return Child(first_name=self.first_name, last_name=self.last_name)


class ChildReadDto(ChildCreateDto):
    uuid: UUID
    first_name: str
    last_name: str

    @classmethod
    def from_domain(cls, child: Child) -> ChildReadDto:
        return ChildReadDto(
            uuid=child.id,
            first_name=child.first_name,
            last_name=child.last_name,
        )


@children_router.get("/{id}")
def get_child(id: UUID) -> ChildReadDto:
    result = ChildGet(ChildInMemoryRepository()).get_child(id)
    if result:
        return ChildReadDto.from_domain(result)
    else:
        raise HTTPException(status_code=404, detail="Child not found")


@children_router.post("/")
def create_child(
    child: ChildCreateDto,
) -> None:
    use_case = ChildCreate(ChildInMemoryRepository())
    use_case.create_child(child.to_domain())
    return
