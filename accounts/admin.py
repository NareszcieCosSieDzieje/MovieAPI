from django.contrib import admin
from .models import Account


@admin.register(Account)
class MovieAdmin(admin.ModelAdmin):
    # list_display = ('user', 'favourite_movies')  # TODO: WHAT ABOUT THE favourite_movies FIELD?
    list_display = ('user', )
