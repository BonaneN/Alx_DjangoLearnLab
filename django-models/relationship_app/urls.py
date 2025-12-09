from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books, LibraryDetailView, register,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book permissions
    path('book/add/', add_book, name='add_book'),
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
]
