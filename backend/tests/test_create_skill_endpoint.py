from django.test import Client


def test_create_skill_returns_created_skill() -> None:
    response = Client().post(
        "/skills/orders",
        data='{"skill_id_str": " test-skill ", "content": "instructions"}',
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.json()["skill_id_str"] == "test-skill"
    assert response.json()["content"] == "instructions"


def test_create_skill_rejects_empty_fields() -> None:
    response = Client().post(
        "/skills/orders",
        data='{"skill_id_str": "", "content": ""}',
        content_type="application/json",
    )

    assert response.status_code == 422
    assert {error["loc"][-1] for error in response.json()["detail"]} == {
        "skill_id_str",
        "content",
    }
