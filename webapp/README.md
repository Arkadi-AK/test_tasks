### Аганесов Аркадий

# Test task app

## Запуск проекта с помощью **docker-compose**
* Склонируйте проект

* Создайте новый образ и запустите два контейнера:
```docker-compose up -d --build```

* Запустите миграции:
```docker-compose exec wb_app python manage.py migrate --noinput```

## Установка и запуск
Склонируйте проект
```bash
python3 -m venv venv
. venv/bin/activate
cd wb_app
pip install -r requirements.txt
```
Переименуйте файл ".env.exsample" в ".env" и введите необходимые данные.

### Запуск
* Примените миграции # ```python manage.py migrate```

Выполните команду, для старта проекта и запуска локального сервера
```python manage.py runserver```

## Использование
* http://127.0.0.1:8000/api/v1/cards/ # адрес для ввода артикулов
