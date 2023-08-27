from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"sprocket", views.SprocketViewSet)
router.register(r"factory", views.FactoryDataViewSet)

urlpatterns = [
    path(r"api/", include(router.urls)),
]
