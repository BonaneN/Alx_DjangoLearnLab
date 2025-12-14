from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow another user"""
        self.following.add(user)
        
    def unfollow(self, user):
        """Unfollow a user"""
        self.following.remove(user)
        
    def is_following(self, user):
        """Check if following a user"""
        return self.following.filter(id=user.id).exists()