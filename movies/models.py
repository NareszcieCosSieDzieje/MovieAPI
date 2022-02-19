from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class Movie(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    id = models.TextField(primary_key=True)
    rank = models.PositiveIntegerField()
    title = models.TextField()
    full_title = models.TextField()
    year = models.TextField()
    image_url = models.TextField()
    crew = models.TextField()
    imbd_rating = models.FloatField()
    imbd_rating_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        movie_str: str = f"Movie<id: {self.id} | rank: {self.rank} | title: {self.title}\n" \
                         f"year: {self.year} | rating: {self.imbd_rating}>"
        return movie_str
