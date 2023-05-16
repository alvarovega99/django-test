# Test Django

Django test, consisting of a REST API that allows creating, modifying, deleting and listing users and products.

Technologies used:
- Django
- Docker
- Postgres
- Postman

## Prerequisites

Before starting, make sure you have the following installed:
- Python 3.x
- Docker

## Download project files

To download the project files, run the following command:

```bash
git clone https://github.com/alvarovega99/django-test.git

```

## Deploy locally using Docker

To deploy the project locally using Docker, run the following commands:

```bash
cd django-test

docker-compose up

```

## Deploy locally without using Docker

To deploy the project locally without using Docker, run the following commands:

```bash
cd django-test

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```
### You must configure the .env file at the root of the project

with the following variables:

- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT


## 

# REST API documentation

### https://documenter.getpostman.com/view/26525060/2s93kxbkgw
