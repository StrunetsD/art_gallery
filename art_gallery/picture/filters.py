import django_filters
from .models import Categoryq,Picture, Author

class PictureFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',  
        lookup_expr='icontains',
        label='Picture Name (contains)'
    )
    author_name = django_filters.CharFilter(
        field_name='author__name',  
        lookup_expr='icontains',
        label='Author Name (contains)'
    )
    start_dt = django_filters.DateTimeFilter(
        field_name="created_at",  
        lookup_expr="gte",  
        label="Start Date (>=)"
    )

    class Meta:
        model = Picture
        fields = ['name', 'author_name', 'created_at']


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )