import os
import re
from functools import reduce
import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from movies.models import Movie


# TODO: LOGGING?
class ImdbApi:

    _api_token = os.environ.get("IMDB_API_TOKEN", "")
    _base_imbd_url = "https://imdb-api.com/en/API/"

    def __init__(self):
        pass

    @staticmethod
    def url_from_parts(*parts: str) -> str:
        def clean_part(part: str) -> str:
            if type(part) is not str or len(part) == 0:
                return ""
            sub_part: str = re.sub(r"/+", "/", part)
            if sub_part[0] == "/":
                sub_part = sub_part[1:]
            if sub_part[-1] != "/":
                sub_part += "/"
            if part_match := re.match(r"(?i)(https?):*/?(.*)", sub_part):
                sub_part = part_match.group(1) + "://" + part_match.group(2)
            return sub_part

        joined_url: str = reduce(lambda p1, p2: p1 + p2, map(clean_part, parts))
        return joined_url

    @staticmethod
    def is_url_valid(url: str) -> bool:
        try:
            URLValidator()(url)
        except ValidationError as e:
            return False
        return True

    # @cache # TODO: a time based cache clean
    def fetch_top_250_movies(self, limit: int = 0) -> list[Movie]:
        top_250_url_part = "Top250Movies"
        top_250_url = self.url_from_parts(self._base_imbd_url, top_250_url_part, self._api_token)

        payload = {}
        headers = {}
        # if limit > 0:
        #     payload['limit'] = limit  # TODO: fetch limit?
        response: requests.Response = requests.request("GET", top_250_url, headers=headers, data=payload)
        response_list: list[dict[str, str]] = response.json().get('items', [])
        kwargs_mapping = {
            'id': 'id',
            'rank': 'rank',
            'title': 'title',
            'fullTitle': 'full_title',
            'year': 'year',
            'image': 'image_url',
            'crew': 'crew',
            'imDbRating': 'imbd_rating',
            'imDbRatingCount': 'imbd_rating_count',
        }
        movie_list: list[Movie] = [Movie(**{kwargs_mapping[k]: v for k, v in movie_dict.items()})
                                   for movie_dict in response_list]
        return movie_list

    def update_top_250_movies(self):
        top_250_movies: list[Movie] = self.fetch_top_250_movies()
        update_fields: list[str] = [
            'rank',
            'title',
            'full_title',
            'year',
            'image_url',
            'crew',
            'imbd_rating',
            'imbd_rating_count',
        ]

        Movie.objects.bulk_update_or_create(top_250_movies, update_fields, match_field='id')


if __name__ == "__main__":
    imdb_api = ImdbApi()
    movie_list: list[Movie] = imdb_api.fetch_top_250_movies()
    from pprint import pprint
    pprint(movie_list)
