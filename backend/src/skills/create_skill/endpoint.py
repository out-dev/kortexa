from uuid import UUID

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from pydantic import BaseModel, Field, ValidationError

from skills.create_skill.use_case import CreateSkillCommand
from skills.dependencies import get_create_skill
from skills.domain.skill import Skill


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
            skill_id_str=skill.skill_id,
            content=skill.content,
        )


@require_POST
def create_skill(request: HttpRequest) -> JsonResponse:
    try:
        payload = CreateSkillRequest.model_validate_json(
            request.body.decode("utf-8")
        )
    except UnicodeDecodeError:
        return JsonResponse(
            {
                "detail": [
                    {
                        "type": "json_invalid",
                        "loc": ["body"],
                        "msg": "Request body must be UTF-8 encoded JSON",
                    }
                ]
            },
            status=422,
        )
    except ValidationError as error:
        detail = [
            {**item, "loc": ["body", *item["loc"]]}
            for item in error.errors()
        ]
        return JsonResponse({"detail": detail}, status=422)

    skill = get_create_skill()(
        CreateSkillCommand(
            skill_id_str=payload.skill_id_str,
            content=payload.content,
        )
    )
    response = SkillResponse.from_domain(skill)
    return JsonResponse(response.model_dump(mode="json"), status=201)