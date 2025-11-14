#!/usr/bin/env python3
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return Book.objects.none()

def list_all_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    # Create sample data for testing
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    book1 = Book.objects.create(title="Harry Potter", author=author1, publication_year=1997)
    book2 = Book.objects.create(title="1984", author=author2, publication_year=1949)
    
    library = Library.objects.create(name="City Central Library")
    library.books.add(book1, book2)
    
    librarian = Librarian.objects.create(name="Alice Johnson", library=library)
    
    # Test queries
    print("Books by J.K. Rowling:")
    for book in query_all_books_by_author("J.K. Rowling"):
        print(f"- {book.title}")
    
    print("\nBooks in City Central Library:")
    for book in list_all_books_in_library("City Central Library"):
        print(f"- {book.title}")
    
    print(f"\nLibrarian for City Central Library: {get_librarian_for_library('City Central Library')}")