
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("user", UserApi, basename= "userapi")

urlpatterns = [
    path("", include(router.urls))

]