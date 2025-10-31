# delete operation

book=Book.objects.get(title="Nineteen Eigthy-Four")
book.delete

Book.objects.all