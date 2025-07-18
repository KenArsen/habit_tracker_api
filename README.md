# 🧠 Habit Tracker API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker)](https://www.docker.com/)

**Современное FastAPI-приложение** для отслеживания привычек с полноценной системой аутентификации, управления привычками и отметками о выполнении.

## 📋 Содержание

- [Возможности](#-возможности)
- [Технологии](#-технологии)
- [Архитектура](#-архитектура)
- [Быстрый старт](#-быстрый-старт)
- [Установка](#-установка)
- [Использование](#-использование)
- [API Документация](#-api-документация)
- [Разработка](#-разработка)
- [Деплой](#-деплой)
- [Лицензия](#-лицензия)

## ✨ Возможности

### Аутентификация и авторизация
- 🔐 Регистрация и вход по email + пароль
- 🍪 JWT авторизация через secure cookies
- 🔒 Смена пароля для авторизованных пользователей
- 👤 Профиль пользователя

### Управление привычками
- ➕ Создание новых привычек
- 📝 Редактирование существующих привычек
- 🗑️ Удаление привычек
- 📊 Просмотр всех привычек пользователя

### Отслеживание выполнения
- ✅ Отметки о выполнении привычек по дате
- 📈 История выполнения привычек
- 📅 Ежедневное отслеживание прогресса

### Административная панель
- 🛠️ SQLAdmin панель для администрирования
- 👥 Управление пользователями
- 📋 Управление привычками и отметками

## 🛠️ Технологии

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - современный веб-фреймворк для создания API
- **[SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/)** - асинхронная ORM
- **[PostgreSQL](https://www.postgresql.org/)** - реляционная база данных
- **[Alembic](https://alembic.sqlalchemy.org/)** - миграции базы данных
- **[Pydantic v2](https://docs.pydantic.dev/)** - валидация данных
- **[SQLAdmin](https://sqladmin.readthedocs.io/)** - административная панель

### DevOps & Инструменты
- **[Docker](https://www.docker.com/)** - контейнеризация
- **[Poetry](https://python-poetry.org/)** - управление зависимостями
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI сервер
- **[Pytest](https://pytest.org/)** - тестирование

## 🏗️ Архитектура

```
app/
├── 🛡️ admin/                    # SQLAdmin views
├── 🌐 api/                      # FastAPI маршруты
│   └── v1/endpoints/           # auth.py, habit.py, checkin.py
├── ⚙️ core/                     # Настройки, БД, безопасность
│   ├── config.py               # Конфигурация приложения
│   ├── database.py             # Подключение к БД
│   └── security.py             # JWT и безопасность
├── 🔄 crud/                     # CRUD-операции
├── 📊 models/                   # SQLAlchemy модели
├── 📝 schemas/                  # Pydantic схемы
├── 🎯 services/                 # Бизнес-логика
├── 🧪 tests/                    # Тесты
└── 📄 main.py                   # Точка входа
```

## 🚀 Быстрый старт

### Docker (Рекомендуется)

```bash
   # Клонирование репозитория
   git clone https://github.com/KenArsen/habit_tracker_api.git
   cd habit_tracker_api

   # Быстрая инициализация проекта
   make init
```

Приложение будет доступно по адресу: **http://localhost:8000**

### Локальная разработка

```bash
   # Установка Poetry
   curl -sSL https://install.python-poetry.org | python3 -

   # Установка зависимостей
   poetry install

   # Настройка окружения
   cp .env.example .env

   # Запуск в режиме разработки
   make dev
```

## 💾 Установка

### Требования
- Python 3.11+
- PostgreSQL 12+
- Docker & Docker Compose (для контейнеризации)

### 1. Клонирование репозитория

```bash
   git clone https://github.com/KenArsen/habit_tracker_api.git
   cd habit_tracker_api
```

### 2. Настройка окружения

```bash
   # Создание .env файла
   cp .env.example .env
```

Отредактируйте `.env` файл с вашими настройками:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_name
DB_USER=db_user
DB_PASS=db_password

JWT_SECRET_KEY=your_secret
JWT_ALGORITHM=HS256
JWT_TOKEN_LOCATION=["cookies"]
JWT_ACCESS_COOKIE_NAME=access_token
CORS_ORIGINS=["http://localhost:8000","http://127.0.0.1:8000"]
```

### 3. Установка зависимостей

#### С Poetry (рекомендуется)
```bash
  poetry install
```

### 4. Настройка базы данных
```bash
# Применение миграций
   make migrate-local

   # Или с Docker
   make docker-migrate
```

## 🎯 Использование

### Запуск приложения

#### Локально
```bash
  make dev
```

#### С Docker
```bash
  make docker-up
```

### Доступные URL

- **API:** http://localhost:8000
- **Документация:** http://localhost:8000/docs (Swagger UI)
- **ReDoc:** http://localhost:8000/redoc
- **Админка:** http://localhost:8000/admin

### Создание суперпользователя
```bash
# Docker
   make docker-create-superuser

   # Локально
   python scripts/create_superuser.py
```

## 📚 API Документация

### Аутентификация

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/api/v1/auth/register` | Регистрация нового пользователя |
| `POST` | `/api/v1/auth/login` | Вход в систему |
| `POST` | `/api/v1/auth/logout` | Выход из системы |
| `GET` | `/api/v1/auth/me` | Получение информации о текущем пользователе |
| `POST` | `/api/v1/auth/change-password` | Смена пароля |

### Управление привычками

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `GET` | `/api/v1/habits` | Получение списка привычек |
| `POST` | `/api/v1/habits` | Создание новой привычки |
| `GET` | `/api/v1/habits/{id}` | Получение привычки по ID |
| `PUT/PATCH` | `/api/v1/habits/{id}` | Обновление привычки |
| `DELETE` | `/api/v1/habits/{id}` | Удаление привычки |

### Отметки выполнения

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/api/v1/checkins` | Создание отметки о выполнении |
| `GET` | `/api/v1/checkins` | Получение отметок пользователя |

Полная документация доступна в Swagger UI: http://localhost:8000/docs

## 🔧 Разработка

### Команды Makefile

#### Основные команды
```bash
   make dev                    # Запуск FastAPI в dev-режиме
   make migration message=""   # Создание новой миграции
   make migrate-local          # Применение миграций локально
   make clean                  # Очистка кэша и Docker
   make init                   # Быстрая инициализация проекта
```

#### Docker команды
```bash
   make docker-build           # Сборка Docker-образов
   make docker-up              # Запуск контейнеров
   make docker-down            # Остановка контейнеров
   make docker-migrate         # Применение миграций в контейнере
   make docker-create-superuser # Создание суперпользователя
   make docker-shell           # Bash внутри контейнера
   make docker-clean           # Полная очистка Docker
```

### Создание миграций
```bash
   # Создание новой миграции
   make migration message="Add new field to User model"

   # Применение миграций
   make migrate-local
```
