from hypothesis import given
import pytest
from dataratz.domain.child import Child
from dataratz.repositories.child_repository import ChildInMemoryRepository
from tests.strategies import child_strategy


@pytest.mark.asyncio
@given(child_strategy)
async def test_add_get(child: Child) -> None:
    repository = ChildInMemoryRepository()
    await repository.add(child)
    result = await repository.get(child.id)
    assert result == child
