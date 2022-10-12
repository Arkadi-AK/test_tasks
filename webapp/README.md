# Notification service

## Установка
```bash
python3 -m venv venv
. venv/bin/activate
cd wb_app
pip install -r requirements.txt
```
Переименуйте файл ".env.exsample" в ".env" и введите необходимые данные.


## Запуск



* Выполните миграции # ```python manage.py makemigrations```
* Примените миграции # ```python manage.py migrate```
* Создайте пользователя # ```python manage.py createsuperuser```

Выполните команду, для старта проекта и запуска локального сервера
```python manage.py runserver```

## Использование