# Docker Makefile для habit_tracker_api

COMPOSE_FILE = docker-compose.yaml
APP_SERVICE = app
DB_SERVICE = db

# Цвета
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
NC = \033[0m

.PHONY: docker-help docker-build docker-up docker-down docker-migrate docker-create-superuser docker-shell docker-clean

# Справка по Docker-командам
docker-help:
	@echo "$(GREEN)📦 Docker команды для $(PROJECT_NAME):$(NC)"
	@echo "  $(GREEN)make docker-build$(NC)            - Сборка Docker-образов"
	@echo "  $(GREEN)make docker-up$(NC)               - Запуск контейнеров"
	@echo "  $(GREEN)make docker-down$(NC)             - Остановка контейнеров"
	@echo "  $(GREEN)make docker-migrate$(NC)          - Применение миграций внутри контейнера"
	@echo "  $(GREEN)make docker-create-superuser$(NC) - Создание суперпользователя"
	@echo "  $(GREEN)make docker-shell$(NC)            - Bash внутри контейнера"
	@echo "  $(GREEN)make docker-clean$(NC)            - Полная очистка Docker и кэша"

# Сборка Docker-образов
docker-build:
	@echo "$(GREEN)🔧 Сборка образов...$(NC)"
	docker-compose -f $(COMPOSE_FILE) build

# Запуск контейнеров
docker-up:
	@echo "$(GREEN)🚀 Запуск контейнеров...$(NC)"
	docker-compose -f $(COMPOSE_FILE) up -d

# Остановка контейнеров
docker-down:
	@echo "$(RED)⛔ Остановка контейнеров...$(NC)"
	docker-compose -f $(COMPOSE_FILE) down

# Выполнение миграций
docker-migrate:
	@echo "$(GREEN)📦 Применение миграций внутри контейнера...$(NC)"
	docker-compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) alembic upgrade head

# Создание суперпользователя
docker-create-superuser:
	@echo "$(GREEN)👤 Создание суперпользователя...$(NC)"
	docker-compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) python /app/scripts/create_superuser.py

# Подключение к bash
docker-shell:
	@echo "$(GREEN)💻 Подключение к контейнеру...$(NC)"
	docker-compose -f $(COMPOSE_FILE) exec $(APP_SERVICE) /bin/bash

# Очистка Docker и Python кэша
docker-clean:
	@echo "$(RED)🧹 Полная очистка...$(NC)"
	docker-compose -f $(COMPOSE_FILE) down --remove-orphans
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
