from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'rank', 'title', 'full_title', 'year', 'image_url', 'crew', 'imbd_rating', 'imbd_rating_count']
