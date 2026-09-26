from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from skills.get_skill.use_case import GetSkill

from skills.adapters.in_memory_skill_repository import (
    InMemorySkillRepository,
)
from skills.create_skill.use_case import CreateSkill


@lru_cache
def get_skill_repository() -> InMemorySkillRepository:
    return InMemorySkillRepository()


RepositoryDep = Annotated[
    InMemorySkillRepository,
    Depends(get_skill_repository),
]


def get_create_skill(
    repository: RepositoryDep,
) -> CreateSkill:
    return CreateSkill(repository)


def get_get_skill(
    repository: RepositoryDep,
) -> GetSkill:
    return GetSkill(repository)


CreateSkillDep = Annotated[
    CreateSkill,
    Depends(get_create_skill),
]

GetSkillDep = Annotated[
    GetSkill,
    Depends(get_get_skill),
]