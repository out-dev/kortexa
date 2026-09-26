from typing import Protocol
from uuid import UUID

from skills.domain.skill import Skill


class SkillRepository(Protocol):
    def add(self, skill: Skill) -> None:
        ...

    def get(self, skill_id: UUID) -> Skill | None:
        ...