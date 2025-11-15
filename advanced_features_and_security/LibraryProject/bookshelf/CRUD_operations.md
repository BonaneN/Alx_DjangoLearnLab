
## Import the Book Class
from bookshelf.models import Book

### Create a book objec with defined attributes
b1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Expected Result: ""
(Return no error when object is created successfully)

### Retrieve Book Object
Book.objects.get(id=product_id)

Expected Output: <Book: 1984 by George Orwell (1949)>

### Update the Book object entry
Book.objects.get(title="1984").update(title="Nineteen Eighty-Four")

Expected Result: 1
(Indicating number of objects updated)

### Delete the Book object entry
Book.objects.filter(publication_year=1949).delete()

Expected Output: (1, {'bookshelf.Book': 1})