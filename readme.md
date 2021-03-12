# Bank security console
Interface to demo database of bank vault visits. Analyzes the information about the vault visits. Detects suspicious visits. Written using [Django Web Framework](https://www.djangoproject.com/)

The project still in development. This file will be updated.

## System requirements:
python3.5+

## How to install:

```bash
git clone https://github.com/KozhevnikovM/devman_django_orm
cd devman_django_orm
pip install -r requirements.txt
```

## Setup your credentials:
Rename ```example.env``` to ```.env``` 
```bash
mv example.env .env
```
and specify it with your credentials:
```
DEBUG= #Debug mode. Default is False.
DB_HOST= #your database address
DB_PORT= #database port
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD= #database password
SECRET_KEY= #Django secret key. Default value is insecure. Please use long random string in production.

```
You can get demo access to database on [dvmn.org](https://dvmn.org/modules/django-orm/). First lesson is free for new students.

## How to run

```bash
python manage.py runserver
```


## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org).
