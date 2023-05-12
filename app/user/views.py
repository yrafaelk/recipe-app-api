from rest_framework import generics
from user.serializers import UserSerialiazer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerialiazer
