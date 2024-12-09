from .models import Comment
from rest_framework import  serializers


class CommentSerializer(serializers.ModelSerializer):
    content_object = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content_object',
            'content', 
            'created_at',
            'updated_at'
            )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
            )