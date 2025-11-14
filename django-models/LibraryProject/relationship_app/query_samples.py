#!/usr/bin/env python3

import os
import django
import sys

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
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
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone", 
        author=author1, 
        defaults={'publication_year': 1997}
    )
    book2, created = Book.objects.get_or_create(
        title="1984", 
        author=author2, 
        defaults={'publication_year': 1949}
    )
    
    library, created = Library.objects.get_or_create(name="City Central Library")
    if created:
        library.books.add(book1, book2)
    
    librarian, created = Librarian.objects.get_or_create(
        name="Alice Johnson", 
        library=library
    )
    
    # Test queries
    print("Books by J.K. Rowling:")
    books_by_rowling = query_all_books_by_author("J.K. Rowling")
    for book in books_by_rowling:
        print(f"- {book.title} ({book.publication_year})")
    
    print("\nBooks in City Central Library:")
    books_in_library = list_all_books_in_library("City Central Library")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
    
    librarian_obj = get_librarian_for_library('City Central Library')
    print(f"\nLibrarian for City Central Library: {librarian_obj}")
    
    if librarian_obj:
        print(f"Librarian name: {librarian_obj.name}")
        print(f"Library: {librarian_obj.library.name}")