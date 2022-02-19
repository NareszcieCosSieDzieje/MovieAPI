from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieList, MovieDetail

app_name = 'movies'

urlpatterns = [
    path('movies/', MovieList.as_view(), name="movies-list"),
    path('movies/<int:pk>/', MovieDetail.as_view(), name="movies-detail"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
