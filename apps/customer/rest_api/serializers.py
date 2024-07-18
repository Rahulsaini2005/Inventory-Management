from rest_framework import serializers

from apps.user.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'