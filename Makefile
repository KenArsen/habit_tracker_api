COMPOSE_FILE = docker/docker-compose.yaml
APP_SERVICE = web
DB_SERVICE = db

# Цвета
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
NC = \033[0m

.PHONY: help

# Справка по Docker-командам
help:
	@echo "$(GREEN)📦 Docker команды для $(PROJECT_NAME):$(NC)"
	@echo "  $(GREEN)make build$(NC)            - Сборка Docker-образов"
	@echo "  $(GREEN)make up$(NC)               - Запуск контейнеров"
	@echo "  $(GREEN)make down$(NC)             - Остановка контейнеров"
	@echo "  $(GREEN)make migrate$(NC)          - Применение миграций внутри контейнера"
	@echo "  $(GREEN)make shell$(NC)            - Bash внутри контейнера"
	@echo "  $(GREEN)make clean$(NC)            - Полная очистка Docker и кэша"

# Сборка Docker-образов
build:
	@echo "$(GREEN)🔧 Сборка образов...$(NC)"
	docker compose -f $(COMPOSE_FILE) build

# Запуск контейнеров
up:
	@echo "$(GREEN)🚀 Запуск контейнеров...$(NC)"
	docker compose -f $(COMPOSE_FILE) up -d

# Остановка контейнеров
down:
	@echo "$(RED)⛔ Остановка контейнеров...$(NC)"
	docker compose -f $(COMPOSE_FILE) down

# Создание таблиц
init-db:
	@echo "$(GREEN)📦 Создание таблицы внутри контейнера...$(NC)"
	docker compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) python3 scripts/init_db.py

# Выполнение миграций
migrate:
	@echo "$(GREEN)📦 Применение миграций внутри контейнера...$(NC)"
	docker compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) alembic upgrade head

# Подключение к bash
shell:
	@echo "$(GREEN)💻 Подключение к контейнеру...$(NC)"
	docker compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) /bin/bash

# Очистка Docker и Python кэша
clean:
	@echo "$(RED)🧹 Полная очистка...$(NC)"
	docker-compose -f $(COMPOSE_FILE) down --remove-orphans
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
