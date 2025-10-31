from hypothesis import given
from dataratz.domain.child import Child
from dataratz.repositories.child_repository import ChildInMemoryRepository
from tests.strategies import child_strategy


@given(child_strategy)
def test_add_get(child: Child) -> None:
    repository = ChildInMemoryRepository()
    repository.add(child)
    result = repository.get(child.id)
    assert result == child