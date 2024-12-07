from rest_framework import  serializers
from .models import Picture,Author

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id','name', 'author','created_at', 'description')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name')