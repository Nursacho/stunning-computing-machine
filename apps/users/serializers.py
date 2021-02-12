from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    avatar = serializers.ImageField(required=False)
    about = serializers.CharField(max_length=255, required=False)
    password1 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'about': self.validated_data.get('about', ''),
            'name': self.validated_data.get('name', ''),
            'avatar': self.validated_data.get('avatar', ''),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('email',)
