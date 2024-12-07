from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Picture(models.Model):
    name=models.CharField(max_length=100, null = False, blank=False)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.TextField(null=True,max_length=200)