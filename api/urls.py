from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet

app_name = "api_v1"

router = DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
