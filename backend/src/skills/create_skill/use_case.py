from dataclasses import dataclass
from typing import Callable
from uuid import UUID, uuid4

from skills.domain.skill import Skill
from skills.ports.skill_repository import SkillRepository


@dataclass(frozen=True, slots=True)
class CreateSkillCommand:
    skill_id_str: str
    content: str


class CreateSkill:
    def __init__(
        self,
        repository: SkillRepository,
        id_factory: Callable[[], UUID] = uuid4,
    ) -> None:
        self._repository = repository
        self._id_factory = id_factory

    def __call__(self, command: CreateSkillCommand) -> Skill:
        skill = Skill.create(
            skill_id=self._id_factory(),
            skill_id_str=command.skill_id_str,
            content=command.content,
        )

        self._repository.add(skill)

        return skill