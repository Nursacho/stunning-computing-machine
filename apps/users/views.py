from django.contrib.auth import get_user_model
from rest_framework import generics

User = get_user_model()
from .serializers import UserSerializer


class ProfileViewSetAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileUpdateViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
