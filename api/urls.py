from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"sprocket/factory", views.SprocketFactoryViewSet
)  # Get sprockets for a given factory id (read only)
router.register(r"sprocket", views.SprocketViewSet)  # CRUD for sprockets
router.register(r"factory", views.FactoryViewSet)  # CRUD for factories

urlpatterns = [
    path(r"api/", include(router.urls)),
]
