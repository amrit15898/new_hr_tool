
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("interview", InterviewApi, basename="interviewapi")

urlpatterns = [
    # path("", IntervieApi.as_view()),
    path("", include(router.urls)),
    path("meeting/" , MeetingApi.as_view())


]