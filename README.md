# О проекте

Тестовое задание для beCloud.<br>
Для реализации БД был использован SQLite, как на стороне бэкенда, так и на стороне микросервиса.<br>
Django работает в DEBUG режиме.<br>

Список библиотек:
```
Django                        ==5.0.2
djangorestframework           ==3.14.0
djangorestframework-simplejwt ==5.3.1
fastapi                       ==0.109.2
pydantic                      ==2.6.1
uvicorn                       ==0.27.1
requests                      ==2.31.0
gunicorn                      ==21.2.0
```

# Запуск

Склонируйте репозиторий:
```shell
git clone git@github.com:hurfy/beCloud.git
```

Создайте и активируйте виртуальное окружение:
```shell
python -m venv venv
venv\Scripts\activate
```

Установите все зависимости:
```shell
pip install -r requirements.txt
```

Соберите Docker-образ микросервиса:
```shell
cd services/store
docker build -t test .
```

Запустите контейнер:
```shell
docker run -d -p 80:80 test
```

Запустите Django-приложение:
```shell
cd core/store
python manage.py runserver
```

# Описание

В данном приложении поддерживаются следующие запросы:

### GET
```
user/profile/ - получение профиля пользователя (только для авторизованных)
products/id?/ - получение списка товаров или по id (только для авторизованных)
```

### POST
```
user/create/  - создание нового пользователя
products/     - создание нового товара (только для авторизованных)
```

### PUT
```
products/id/  - изменение товара по id (только для авторизованных)
```

### DELETE
```
products/id?/ - удаление всех товаров или по id (только для авторизованных)
```

### TOKENS
```
api/token/         - получение JWT токена
api/token/refresh/ - обновление токена
api/token/verify/  - верификация токена
```
