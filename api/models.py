from django.db import models

# Create your models here.

# Create an Author model representing book authors
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Create a Book model linked to the Author model via a ForeignKey
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books'   )

    def __str__(self):
        return self.title