# update operation
from bookshelf import Book

book=Book.objects.get(title="1984")
book.title = "Nineteen Eigthy-Four"
book.save()
book