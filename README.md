# MovieAPI is a Django(3) REST_API project.

## Tech stack:
- nginx | reverse proxy
- letsencrypt | SSL encryption
- gunicorn | WSGI HTTP server
- django | HTTP server
- celery | asynchronous task broker
- docker, docker-compose | virtualization

<h3>
The celery broken periodically fetches and updates 
the server's database using the top 250 movies API by IMDB. 
</h3>

## Users can register and then add movies to favourites.

### Tested with:
    - debian-bullseye
    - docker-compose 3
    - Python 3.10.2 
