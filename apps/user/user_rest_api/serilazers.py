from rest_framework import serializers


from apps.user.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','user_type']