from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create', BookCreateView.as_view(), name='book-create'),  # remove trailing slash
    path('books/update', BookUpdateView.as_view(), name='book-update'),  # exactly "books/update"
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),  # exactly "books/delete"
]
