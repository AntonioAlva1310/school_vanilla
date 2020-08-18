from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subjects.views import SubjectViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
