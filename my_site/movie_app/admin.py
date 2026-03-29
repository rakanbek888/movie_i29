from django.contrib import admin
from .models import (UserProfile, Category, Country, Director, Actor,
                     Genre, Movie, MovieLanguages, Moments,
                     Rating, Review, ReviewLike, Favorite, FavoriteMovie, History)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'status', 'phone_number']
    list_filter = ['status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['director_name', 'age']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['actor_name', 'age']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['Genre_name', 'category']


class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MomentsInline(admin.TabularInline):
    model = Moments
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguagesInline, MomentsInline]
    list_display = ['movie_name', 'year', 'types', 'movie_time', 'status_movie']
    list_filter = ['types', 'status_movie', 'genre']
    search_fields = ['movie_name']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'star']
    list_filter = ['star']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'created_date']


@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'like']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ['favorite', 'movie']


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'viewed_at']