from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()

router.register('teams', views.ListTeamView)
router.register('programmers', views.ListProgrammerView)
router.register('languages', views.ListLanguageView)
router.register('paradigms', views.ListParadigmView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^programmers/(?P<programmer_id>[0-9]+)/languages/rel/(?P<language_id>[0-9]+)', views.programmer_language_rel),
    url(r'^languages/(?P<language_id>[0-9]+)/paradigms/rel/(?P<paradigm_id>[0-9]+)', views.language_paradigm_rel),
]
