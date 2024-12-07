from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from user import views as user_views    
from gallery.views import GalleryListView    
from user.views import UserRegisterView, UserLoginView, UserLogoutView


router = DefaultRouter()
router.register(r'api/gallery/list', GalleryListView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/user/login/', UserLoginView.as_view(), name='user_login'),
    path('api/user/logout/', UserLogoutView.as_view(), name='user_logout'),
] + router.urls
