from uuid import UUID

from fastapi import APIRouter, status
from pydantic import BaseModel, Field

from skills.create_skill.use_case import CreateSkillCommand
from skills.dependencies import CreateSkillDep
from skills.domain.skill import Skill

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


class CreateSkillRequest(BaseModel):
    skill_id_str: str = Field(min_length=1)
    content: str = Field(min_length=1)


class SkillResponse(BaseModel):
    id: UUID
    skill_id_str: str
    content: str

    @classmethod
    def from_domain(cls, skill: Skill) -> "SkillResponse":
        return cls(
            id=skill.id,
            skill_id_str=skill.skill_id_str,
            content=skill.content,
        )


@router.post(
    "",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_skill(
    request: CreateSkillRequest,
    use_case: CreateSkillDep,
) -> SkillResponse:
    skill = use_case(
        CreateSkillCommand(
            skill_id_str=request.skill_id_str,
            content=request.content,
        )
    )

    return SkillResponse.from_domain(skill)