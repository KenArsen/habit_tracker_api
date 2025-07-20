# Этап 1: Сборка зависимостей с Poetry
FROM python:3.12-slim AS builder

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /habit_tracker_api

# Устанавливаем Poetry
RUN pip install poetry

# Копируем только файлы Poetry для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости без dev
RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi --no-root

# Копируем весь проект
COPY . /habit_tracker_api

# Этап 2: Runtime-образ
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /habit_tracker_api

# Устанавливаем минимальные системные зависимости (для Celery, PostgreSQL и т.д.)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и проект из builder
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /habit_tracker_api /habit_tracker_api

# Открываем порт для Django
EXPOSE 8000

# Указываем команду по умолчанию (будет переопределена в docker-compose)
CMD ["sh", "-c", " uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
