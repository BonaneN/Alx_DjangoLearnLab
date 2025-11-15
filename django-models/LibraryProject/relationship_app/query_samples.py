import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library.name}: {[book.title for book in library.books.all()]}")
    except Library.DoesNotExist:
        print(f"No library named {library_name}")
        return

    # Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library.name}")


if __name__ == "__main__":
    run_queries()
