from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    address = models.TextField()
    books = models.ManyToManyField(Book, related_name='stores')

    def __str__(self):
        return self.store_name
