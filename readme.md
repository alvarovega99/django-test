# Test Django

##

Test de Django, consistente en una API REST que permite crear, modificar, eliminar y listar usuarios y productos.

Tecnologías utilizadas:

- Django
- Docker
- Postgres
- Postman


##

## Requisitos previos

Antes de empezar, asegúrate de tener instalado lo siguiente:

- Python 3.x
- Docker

## Descargar archivos del proyecto

Para descargar los archivos del proyecto, ejecuta el siguiente comando:

```bash
git clone https://github.com/alvarovega99/django-test.git
```

## Despliegue en local utilizando Docker

Para desplegar el proyecto en local utilizando Docker, ejecuta los siguientes comandos:

```bash
cd django-test

docker-compose up
```

## Despliegue en local sin utilizar Docker

Para desplegar el proyecto en local sin utilizar Docker, ejecuta los siguientes comandos:

```bash
cd django-test

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## 

# Documentación de la API REST

### https://documenter.getpostman.com/view/26525060/2s93kxbkgw
