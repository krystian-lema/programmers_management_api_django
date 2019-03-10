from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('teams', views.ListTeamView)
router.register('programmers', views.ListProgrammerView)
router.register('languages', views.ListLanguageView)
router.register('paradigms', views.ListParadigmView)

urlpatterns = [
    path('', include(router.urls))
]
