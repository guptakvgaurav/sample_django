from django.db import models


# Create your models here.
class Author(models.Model):

    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    age = models.IntegerField(blank=True)
    designation = models.TextField(blank=True)
    aadhar_id = models.IntegerField(unique=True)
    token = models.TextField(blank=True)
