from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Test the relationship queries'

    def handle(self, *args, **options):
        # Clear existing sample data to avoid duplicates
        Librarian.objects.filter(name="Alice Johnson").delete()
        Library.objects.filter(name="City Central Library").delete()
        Book.objects.filter(title__in=["Harry Potter and the Philosopher's Stone", "1984"]).delete()
        Author.objects.filter(name__in=["J.K. Rowling", "George Orwell"]).delete()
        
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
        self.stdout.write("Books by J.K. Rowling:")
        books_by_rowling = Book.objects.filter(author__name="J.K. Rowling")
        for book in books_by_rowling:
            self.stdout.write(f"- {book.title} ({book.publication_year})")
        
        self.stdout.write("\nBooks in City Central Library:")
        books_in_library = library.books.all()
        for book in books_in_library:
            self.stdout.write(f"- {book.title} by {book.author.name}")
        
        try:
            librarian_obj = Librarian.objects.get(library=library)
            self.stdout.write(f"\nLibrarian for City Central Library: {librarian_obj.name}")
            self.stdout.write(f"Library: {librarian_obj.library.name}")
        except Librarian.DoesNotExist:
            self.stdout.write("\nNo librarian found for this library")