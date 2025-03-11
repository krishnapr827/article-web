from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=120)
    desc=models.TextField()
    author=models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title