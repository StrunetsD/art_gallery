from django.shortcuts import render
from rest_framework import viewsets
from .models import Picture, Author
from .serializer import AuthorSerializer, PictureSerializer


class PictureListView(viewsets.ModelViewSet):
    queryset=Picture.objects.all()
    serializer_class=PictureSerializer
    permission_classes=()
    
class AuthorListView(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=()

