from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile
from .views import (
    PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/new", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete")
]