
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # max length 200 chars
    author = models.CharField(max_length=100) # max length 100 chars
    publication_year = models.IntegerField()  # integer year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
