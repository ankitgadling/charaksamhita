from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ebook(models.Model):
    title=models.CharField(max_length=50)
    book=models.FileField(upload_to="media")

    def __str__(self):
        return self.title