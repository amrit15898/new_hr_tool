
from django.urls import path, include
from .views import *
urlpatterns = [
    path("", users_api.as_view())

]