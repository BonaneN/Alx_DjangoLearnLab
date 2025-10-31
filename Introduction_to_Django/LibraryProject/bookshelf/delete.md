# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book and delete it
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
