from django.shortcuts import render
from django.views.generic import DetailView  # Make sure this import exists
from .models import Book, Library  # Make sure Library is imported

# Function-based view that lists all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view that displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # This requires Library import
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
