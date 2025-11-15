

from bookshelf.models import Book

Book.objects.get(title="1984").update(title="Nineteen Eighty-Four")

["book.title", "Nineteen Eighty-Four"]

Returns: 1 (Indicating number of objects updated)