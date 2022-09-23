from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, OrderViewSet

app_name = "api_v1"

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]
