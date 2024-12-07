from rest_framework import  serializers
from .models import Gallery
from picture.serializer import PictureSerializer




class GallerySerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'description', 'created_at', 'pictures')