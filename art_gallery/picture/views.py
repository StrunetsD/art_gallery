from django.shortcuts import render
from rest_framework import viewsets
from .models import Picture, Author, Category
from .serializer import AuthorSerializer, PictureSerializer, CategorySerializer
from .filters import PictureFilter, AuthorFilter, CategoryFilter


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = ()
    filterset_class = CategoryFilter


class PictureListView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = ()
    filterset_class = PictureFilter
    
    
class AuthorListView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ()
    filterset_class = AuthorFilter

