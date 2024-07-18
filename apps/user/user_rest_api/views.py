import uuid

from django.contrib.auth import authenticate
from rest_framework import viewsets, status

from apps.user.models import User, UserToken
from apps.user.user_rest_api.serilazers import UserSerializers, LoginSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

# class LoginViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer








# class RegisterUser(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data  = request.data)
#         if not serializer.is_valid():
#             return Response({'status':403,'errors':serializer.errors,'message':'something with  wrong'})
#         serializer.save()
#         user = User.objects.get()
#         token_obj ,_ = Token.objects.get_or_create(user=user)
#         return Response({'status':200,'errors':serializer.data,'token':str(token_obj),'message':'your data saved'})