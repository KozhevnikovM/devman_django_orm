# Пульт охраны банка
Интерфейс к базе данных о посещениях банковского хранилища. Анализирует информацию о посещении хранилища. Выявляет подозрительные посещения.

## System requirements:
python3.5+

## How to install:

```bash
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
```

## How to run

```bash
python manage.py runserver
```


## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org).
