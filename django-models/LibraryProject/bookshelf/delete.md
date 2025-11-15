from bookshelf.models import Book

Book.objects.filter(publication_year=1949).delete()

["book.delete"]

Returns: (1, {'bookshelf.Book': 1})