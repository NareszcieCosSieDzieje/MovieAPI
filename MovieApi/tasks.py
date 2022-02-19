from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def update_top_250_movies():
    from imdb_api.data_fetcher import ImdbApi
    imbd_api = ImdbApi()
    imbd_api.update_top_250_movies()
    logger.info(f"The 'update_top_250_movies' task just ran.")
