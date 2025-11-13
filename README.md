# Wallet

## Описание
Простое асинхронное API для работы с базой данных. Работает в двух контейнерах: первый — для серверной части, второй — для базы данных.

## Технологии
- FastAPI + granian
- PostgresSQL + asyncpg

## Запуск приложения
Клонируй репозиторий с проектом.
```bash
git clone git@github.com:KlimovArtem/wallet.git
```
Перейди в корневую папку проекта и выполни команду сборки приложения из docker-compose файла.
```bash
docker compose up -f docker-compose.yml -d
```

> <u>Примечание</u>:

> Для запуска приложения требуется файл с переменными окружения .env который содержит данные для подключения к БД
> ```
> DB_URL=postgres://user_name:password@host_name/db_name
> ```
