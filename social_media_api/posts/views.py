from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from permissions import IsOwnerOrReadOnly
from typing import Any
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Post CRUD
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Comment CRUD
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self)->Any:
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self)->Any:
        user:CustomUser = self.request.user
        return Post.objects.filter(user__in=self.request.user.following.all()).order_by('-created_at')
