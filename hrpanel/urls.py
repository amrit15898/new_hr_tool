
from django.urls import path, include
from .views import *
urlpatterns = [
    path("", IntervieApi.as_view()),
    path("/meeting" , MeetingApi.as_view())


]