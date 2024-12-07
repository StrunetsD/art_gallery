from rest_framework.response import Response
from rest_framework import viewsets
from .models import Gallery
from .serializer import *


class GalleryListView(viewsets.ModelViewSet):
    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer
    permission_classes = ()

    
    