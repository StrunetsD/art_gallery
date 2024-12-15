from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from gallery.views import GalleryListView, GallerySearchResultsView    
from user.views import UserRegisterView, UserLoginView, UserLogoutView
from picture.views import PictureListView, AuthorListView, ExhibitionListView, CategoryListView
from comment.views import CommentView


router = DefaultRouter(trailing_slash=True)
router.register(r'api/categories', CategoryListView)
router.register(r'api/galleries', GalleryListView)
router.register(r'api/authors',AuthorListView)
router.register(r'api/pictures',PictureListView)
router.register(r'api/exhibitions', ExhibitionListView)

urlpatterns = [
    path('api/comments/',CommentView.as_view(),name='comments'),
    path('api/user/login/', UserLoginView.as_view(), name='user_login'),
    path('api/user/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('gallery/search/', GallerySearchResultsView.as_view(), name='gallery_search_results'),
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),
] + router.urls
