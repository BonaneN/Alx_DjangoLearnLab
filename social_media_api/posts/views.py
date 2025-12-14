from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import isOwnerOrReadOnly
from typing import Any

class PostViewSet(viewsets.ModelViewSet):
    queryset = PostSerializer
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self)->Any:
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]

    def get_queryset(self)->Any:
        return Comment.objects.filter(post_id=self.kwargs['post_pk']).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])