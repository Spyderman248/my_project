from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    publication = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)


# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     bio = models.TextField()
#     date_of_birth = models.DateField()

    def __str__(self):
        return self.title

# Create your models here.
