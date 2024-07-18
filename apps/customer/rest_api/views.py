from rest_framework import viewsets

from apps.customer.rest_api.serializers import CustomerSerializer
from apps.user.models import User


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer


