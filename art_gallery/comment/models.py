from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comment(models.Model):
    user = models.ForeignKey(
       'user.User', 
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  
    object_id = models.PositiveIntegerField()  
    content_object = GenericForeignKey("content_type", "object_id") 
    content = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.content_object}"
