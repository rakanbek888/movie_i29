import django_filters
from .models import Movie, Country, Genre, Actor, Director


class MovieFilter(django_filters.FilterSet):
    country = django_filters.ModelMultipleChoiceFilter(
        queryset=Country.objects.all(),
        field_name='country',
    )
    genre = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        field_name='genre',
    )
    actor = django_filters.ModelMultipleChoiceFilter(
        queryset=Actor.objects.all(),
        field_name='actor',
    )
    director = django_filters.ModelMultipleChoiceFilter(
        queryset=Director.objects.all(),
        field_name='director',
    )
    status_movie = django_filters.CharFilter(
        field_name='status_movie',
        lookup_expr='icontains'
    )

    class Meta:
        model = Movie
        fields = ['country', 'genre', 'actor', 'director', 'status_movie']