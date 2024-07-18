from django.urls import path, include
from rest_framework import routers
from apps.customer.rest_api.views import CustomerViewSet

app_name = "customer"

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns =[
    path('',include(router.urls)),

]