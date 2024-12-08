from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=100, null = False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,max_length=200)
    gallery = models.ForeignKey('gallery.Gallery', on_delete=models.CASCADE, related_name='pictures', null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Exhibition(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    pictures = models.ManyToManyField(Picture, related_name='exhibitions') 

    def __str__(self):
        return self.name