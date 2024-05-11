# Create your models here.
from django.db import models

class Comment(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
