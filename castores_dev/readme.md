# PROYECTO CASTORES_TI

 IDE utilizado - Visual Studio Code
 Versión del lenguaje de programación utilizado - Python3, Django last version
 DBMS utilizado y su versión - Mysql https://dbeaver.com/docs/dbeaver/Database-driver-MySQL

 Lista de pasos para correr su aplicación -
 Se debe de tener instalado Python, Django, Docker
 Siguiendo los comandos de abajo se corre el proyecto. 

## Herramientas
- Django
- Contenedor Docker
- HTML
- CSS
- JS
- Bootstrap
- MySQL


## Correr el sistema en pruebas
docker-compose up --build

docker-compose exec app bash

python3 manage.py check

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 0:8000

## Instalar requerimientos 
python3 manage.py -r requirements.txt

## Limpiar base de datos y docker

docker container prune

docker image prune -f

docker volume prune -f

docker network prune

docker system prune

docker system prune --volumes -f
