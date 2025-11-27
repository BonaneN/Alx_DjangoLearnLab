from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import NotFound
from django_filters import rest_framework
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer


# List all books - read-only for everyone
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Retrieve a single book - read-only for everyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book - authenticated users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Update an existing book - authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):  # type: ignore
        book_id = self.request.GET.get('id')
        if not book_id:
            raise NotFound("Book ID is required")
        return get_object_or_404(Book, pk=book_id)


# Delete a book - authenticated users only
class BookDeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):  # type: ignore
        book_id = self.request.GET.get('id')
        if not book_id:
            raise NotFound("Book ID is required")
        return get_object_or_404(Book, pk=book_id)
