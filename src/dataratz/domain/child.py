from dataclasses import  dataclass, field
from uuid import UUID, uuid4


@dataclass
class Child:
    first_name: str
    last_name: str
    id: UUID = field(default_factory=uuid4)
