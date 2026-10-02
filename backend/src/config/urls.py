from django.urls import path

from skills.create_skill.endpoint import create_skill

urlpatterns = [
    path("skills/orders", create_skill, name="create_skill"),
]
