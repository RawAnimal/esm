from django.urls import path, include
from project.api.views import project_list, project_details

urlpatterns = [
    path("", project_list, name="project-list"),
    path("<int:pk>", project_details, name="project-details"),
]
