from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User
from .models import Comment  
from picture.models import Picture, Author
from django.urls import reverse


class CommentViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='testname')
        self.picture = Picture.objects.create(name='Test Picture', description='Test Description', author=self.author)
        self.url = reverse('comment-list', args=[self.picture.id])  

    def test_create_comment_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'This is a test comment.')

    
    def test_create_comment_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'This is a test comment.')

    def test_create_comment_picture_not_found(self):
        self.client.login(username='testuser', password='testpass') 
        invalid_url = reverse('comment-list', args=[999])  
        data = {
            'content': 'This comment will not be saved.'
        }
        response = self.client.post(invalid_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 
        self.assertEqual(response.data, {'error': 'Picture not found'})

    def test_create_comment_unauthenticated(self):
        data = {
            'content': 'This comment should not be saved.'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  

    def test_create_comment_invalid_data(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'content': ''  
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  
        self.assertIn('content', response.data)