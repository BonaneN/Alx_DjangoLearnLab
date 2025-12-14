# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

class User(AbstractUser):
    """
    Custom user model that supports following other users.
    'following' is the set of users this user follows.
    'followers' is the reverse relation (users who follow this user).
    """
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def follow(self, user):
        """Follow the provided user (no-op if already following)."""
        if user and user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow the provided user (no-op if not following)."""
        if user and user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(pk=user.pk).exists()
