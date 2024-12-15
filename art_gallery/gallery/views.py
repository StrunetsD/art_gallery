from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gallery
from .serializer import *


class GalleryListView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = ()


class GallerySearchResultsView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']  
