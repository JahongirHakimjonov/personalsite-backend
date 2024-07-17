from django.urls import path

from apps.portfolio.views import (
    ContactInfoView,
    EducationView,
    ExperienceView,
    HomeView,
    ProjectsView,
    SkillView,
    SupportView,
)

urlpatterns = [
    path("index/", HomeView.as_view(), name="home"),
    path("contact/", ContactInfoView.as_view(), name="contact"),
    path("education/", EducationView.as_view(), name="education"),
    path("experience/", ExperienceView.as_view(), name="experience"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("skills/", SkillView.as_view(), name="skills"),
    path("support/", SupportView.as_view(), name="support"),
]
