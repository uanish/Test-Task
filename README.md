# Запуск проекта

Для первого запуска проекта необходимо:
1. Скачать проект с репозитория
2. В корне проекта: **docker-compose up -d --build**
3. Затем работа с миграциями:
    - **docker-compose exec app poetry run alembic revision --autogenerate -m "Create Tables"**
    - **docker-compose exec app poetry run alembic upgrade head**
4. Сайт будет доступен по адресу: **http://localhost:8000/docs**

5. Для запуска тестов: после действий выше выполнить: **docker-compose run --rm tests**