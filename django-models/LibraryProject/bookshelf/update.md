# Update Operation

```python
from bookshelf.models import Book

# Retrieve and update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book
