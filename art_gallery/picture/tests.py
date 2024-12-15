from rest_framework.test import APITestCase
from rest_framework import status
from django.core.cache import cache
from .models import Picture, Author, Category, Exhibition

class CategoryListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Category 1")
        Category.objects.create(name="Category 2")

    def setUp(self):
        cache.clear()

    def test_category_list(self):
        response = self.client.get('/api/categories/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)



class PictureListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name="Author 1")  
        Picture.objects.create(name="Picture 1", description="Description 1", author=author)
        Picture.objects.create(name="Picture 2", description="Description 2", author=author)
                               
    def test_picture_list(self):
        response = self.client.get('/api/pictures/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_picture_list_cache(self):
        cache_key = 'picture_list'
        cache.set(cache_key, [{'title': 'Cached Picture', 'description': 'Cached Description'}])

        response = self.client.get('/api/pictures/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Cached Picture')


class AuthorListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name="Author 1")
        Author.objects.create(name="Author 2")

    def test_author_list(self):
        response = self.client.get('/api/authors/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_author_list_cache(self):
        cache_key = 'author_list'
        cache.set(cache_key, [{'name': 'Cached Author'}])

        response = self.client.get('/api/authors/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Cached Author')


class ExhibitionListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Exhibition.objects.create(name="Exhibition 1", end_dt="2024-12-31T23:59:59Z")
        Exhibition.objects.create(name="Exhibition 2", end_dt="2025-01-01T00:00:00Z")


    def test_exhibition_list(self):
        response = self.client.get('/api/exhibitions/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_exhibition_list_cache(self):
        cache_key = 'exhibition_list'
        cache.set(cache_key, [{'title': 'Cached Exhibition'}])

        response = self.client.get('/api/exhibitions/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Cached Exhibition')
