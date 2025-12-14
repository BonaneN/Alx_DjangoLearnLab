
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView,
from django.contrib import admin,
from django.urls import path, include,
from .views import RegisterView, LoginView,


# DRF router for posts and comments
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),  # ✅ This is the required feed route
    path('unfollow/<int:user_id>/', UserProfileView.as_view(), name='unfollow'),
      # include accounts app URLs
     path('register/', RegisterView.as_view(), name='register'),  # /register/
    path('login/', LoginView.as_view(), name='login'),           # /login/
    path('profile/', lambda request: None, name='profile'),   
    path('accounts/', include('accounts.urls')),

]
