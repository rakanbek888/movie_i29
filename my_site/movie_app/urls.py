from django.urls import path, include
from rest_framework import routers
from .views import (
    UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, CountryListAPIView, CountryDetailAPIView,
    DirectorListAPIView, DirectorDetailAPIView, ActorListAPIView, ActorDetailView, GenreListAPIView,
    MovieListAPIView, RatingViewSet, ReviewViewSet, ReviewLikeViewSet,
    FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, GenreDetailAPIView, MovieDetailAPIView, RegisterView,LoginView, LogoutView,
)

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'review-likes', ReviewLikeViewSet, basename='review-like')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'favorite-movies', FavoriteMovieViewSet, basename='favorite-movie')
router.register(r'history', HistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),

     path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),

]