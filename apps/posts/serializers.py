from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description')


class PostGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
