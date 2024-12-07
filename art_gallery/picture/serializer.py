from rest_framework import  serializers
from .models import Picture, Author, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','name',)


class PictureSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Picture
        fields = ('id','name', 'author','created_at', 'description','category')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id','name')