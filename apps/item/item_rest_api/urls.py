from django.urls import path, include
from rest_framework import routers

from apps.item.item_rest_api.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]