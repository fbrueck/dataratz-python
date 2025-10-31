from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class CampPart:
    id: UUID = field(default_factory=uuid4)

@dataclass
class Camp:
    id: UUID = field(default_factory=uuid4)
    camps_parts: list[CampPart]
