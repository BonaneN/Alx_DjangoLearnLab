from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView, profile, search, posts_by_tag
from .views import (
    PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path("", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add_comments"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    path("search/", search, name="search_results"),
    path("tags/<str:tag_name>/", posts_by_tag, name="posts_by_tag"),
]