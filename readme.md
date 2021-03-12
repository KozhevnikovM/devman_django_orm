# Bank security console
Interface to demo database of bank vault visits. Analyzes the information about the vault visits. Detects suspicious visits. Written using [Django Web Framework](https://www.djangoproject.com/)

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
SECRET_KEY= #Django secret key. 
DB_HOST= #your database address
DB_PORT= #database port
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD= #database password

```

## How to run

```bash
python manage.py runserver
```


## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org).
