from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Picture, Author, Category, Exhibition
from .serializer import AuthorSerializer, PictureSerializer, CategorySerializer, ExhibitionSerializer
from .filters import PictureFilter, AuthorFilter, CategoryFilter, ExhibitionFilter

class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = ()
    filterset_class = CategoryFilter

    def list(self, request, *args, **kwargs):
        cache_key = 'category_list'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 15) 
        return response


class PictureListView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = ()
    filterset_class = PictureFilter

    def list(self, request, *args, **kwargs):
        cache_key = 'picture_list'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 15)  
        return response


class AuthorListView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = ()
    filterset_class = AuthorFilter

    def list(self, request, *args, **kwargs):
        cache_key = 'author_list'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 15)  
        return response


class ExhibitionListView(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = ()
    filterset_class = ExhibitionFilter

    def list(self, request, *args, **kwargs):
        cache_key = 'exhibition_list'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 15) 
        return response