import pytest
from dataratz.domain.child import Child
from dataratz.repositories.child_repository import ChildInMemoryRepository
from dataratz.use_cases.child_use_cases import ChildCreate, ChildGet
from tests.strategies import child_strategy
from hypothesis import given


@pytest.mark.asyncio
@given(child_strategy)
async def test_create_get(child: Child) -> None:
    repository = ChildInMemoryRepository()
    await ChildCreate(child_repsoitory=repository).create_child(child)
    result = await ChildGet(child_repsoitory=repository).get_child(child.id)
    assert result == child
