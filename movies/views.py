from django.shortcuts import render

from rest_framework import mixins
from rest_framework import filters
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from utils.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


class MovieList(generics.ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'year']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MovieDetail(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
