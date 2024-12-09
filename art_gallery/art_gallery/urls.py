from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from gallery.views import GalleryListView    
from user.views import UserRegisterView, UserLoginView, UserLogoutView
from picture.views import PictureListView, AuthorListView, ExhibitionListView

router = DefaultRouter(trailing_slash=True)
router.register(r'api/gallery_list', GalleryListView)
router.register(r'api/author_list',AuthorListView)
router.register(r'api/picture_list',PictureListView)
router.register(r'api/exhibition_list', ExhibitionListView)
urlpatterns = [
    path('api/user/login/', UserLoginView.as_view(), name='user_login'),
    path('api/user/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),
] + router.urls
