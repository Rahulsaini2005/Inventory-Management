from django.urls import path, include
from rest_framework import routers

from apps.product.product_rest_api.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]

