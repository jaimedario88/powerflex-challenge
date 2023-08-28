from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"sprocket/factory", views.SprocketFactoryViewSet)
router.register(r"sprocket", views.SprocketViewSet)
router.register(r"factory", views.FactoryViewSet)

urlpatterns = [
    path(r"api/", include(router.urls)),
]
