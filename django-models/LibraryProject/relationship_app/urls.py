from django.urls import path
from . import views
from .views import LibraryDetailView  # Import the class-based view

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),
    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]