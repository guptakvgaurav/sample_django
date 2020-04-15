from django.db import models

from author.models import Author


# Create your models here.
class Article(models.Model):

    title = models.TextField(max_length=255, blank=False)
    url = models.URLField(blank=True)
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE)

