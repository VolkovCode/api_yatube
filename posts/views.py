from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
                          permissions.IsAuthenticated,
                          IsOwnerOrReadOnly
                        ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet): 
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])
    serializer_class = CommentSerializer
    permission_classes = [
                          permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                        ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
