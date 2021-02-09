from rest_framework import viewsets
from .serializers import PostSerializer, PostGetSerializer
from .models import Post


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostGetSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostGetSerializer
        return PostSerializer

