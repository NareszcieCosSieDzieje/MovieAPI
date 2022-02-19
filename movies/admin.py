from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rank',
        'title',
        'full_title',
        'year',
        'image_url',
        'crew',
        'imbd_rating',
        'imbd_rating_count',
    )

