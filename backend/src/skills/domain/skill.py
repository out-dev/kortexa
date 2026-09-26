from dataclasses import dataclass
from enum import StrEnum
from uuid import UUID


class SkillStatus(StrEnum):
    CREATED = "created"


@dataclass(frozen=True, slots=True)
class Skill:
    id: UUID
    skill_id: str
    content: str
    status: SkillStatus

    @classmethod
    def create(
        cls,
        *,
        skill_id: UUID,
        skill_id_str: str,
        content: str,
    ) -> "Skill":
        skill_id_str = skill_id_str.strip()

        if not skill_id_str:
            raise ValueError("skill_id must not be empty")

        if not content:
            raise ValueError("content must not be empty")

        return cls(
            id=skill_id,
            skill_id=skill_id_str,
            content=content,
            status=SkillStatus.CREATED,
        )