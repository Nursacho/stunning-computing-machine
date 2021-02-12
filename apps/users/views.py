from rest_auth import views
from rest_auth.registration import views as register
from rest_framework import viewsets, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer


class CustomRegisterView(register.RegisterView):
    queryset = User.objects.all()
    serializer_class = CustomRegisterSerializer


class CustomLoginView(views.LoginView):
    user_serializer_class = CustomUserDetailsSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(email=request.data[User.USERNAME_FIELD])
            serialized_user = self.user_serializer_class(user)
            response.data.update(serialized_user.data)
        return response


class CustomLoginViewJWT(TokenObtainPairView):
    user_serializer_class = CustomUserDetailsSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(email=request.data[User.USERNAME_FIELD])
            serialized_user = self.user_serializer_class(user)
            response.data.update(serialized_user.data)
        return response


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserDetailsSerializer
