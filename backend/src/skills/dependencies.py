from functools import lru_cache

from skills.adapters.in_memory_skill_repository import (
    InMemorySkillRepository,
)
from skills.create_skill.use_case import CreateSkill


@lru_cache
def get_skill_repository() -> InMemorySkillRepository:
    return InMemorySkillRepository()


def get_create_skill() -> CreateSkill:
    return CreateSkill(get_skill_repository())