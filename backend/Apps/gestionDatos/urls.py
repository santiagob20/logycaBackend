from django.urls import path, include
from .import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('student', views.StudentView)
router.register('professor', views.ProfessorView)
router.register('score', views.ScoreView)


urlpatterns = [
    path('', include(router.urls))
]
