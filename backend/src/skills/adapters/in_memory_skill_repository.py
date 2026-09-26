from threading import RLock
from uuid import UUID

from skills.domain.skill import Skill


class InMemorySkillRepository:
    def __init__(self) -> None:
        self._skills: dict[UUID, Skill] = {}
        self._lock = RLock()

    def add(self, skill: Skill) -> None:
        with self._lock:
            self._skills[skill.id] = skill

    def get(self, skill_id: UUID) -> Skill | None:
        with self._lock:
            return self._skills.get(skill_id)