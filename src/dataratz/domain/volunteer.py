from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Volunteer:
    id: UUID = field(default_factory=uuid4)

@dataclass
class VolunteerAssignment:
    id: UUID = field(default_factory=uuid4)
    volunteer_id: UUID
    camp_id: UUID
