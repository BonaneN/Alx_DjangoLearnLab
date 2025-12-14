from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like

User = get_user_model()

# -------------------
# Like Serializer
# -------------------
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']  # removed the extra comma


# -------------------
# Comment Serializer
# -------------------
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", queryset=User.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Comment
        fields = ["id", "post", "content", "author", "author_id", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def create(self, validated_data):
        # If author provided via author_id, it will be set; otherwise, expect view to set request.user
        return super().create(validated_data)


# -------------------
# Post List Serializer
# -------------------
class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "author", "comments_count", "created_at", "updated_at"]


# -------------------
# Post Detail Serializer
# -------------------
class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "comments", "created_at", "updated_at"]
        read_only_fields = ["author", "created_at", "updated_at"]
