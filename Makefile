DOCKER_COMPOSE = docker compose
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
	@echo "  $(GREEN)make watch$(NC)            - Наблюдение за файлами и автоматическая пересборка"
	@echo "  $(GREEN)make down$(NC)             - Остановка контейнеров"
	@echo "  $(GREEN)make shell$(NC)            - Bash внутри контейнера"
	@echo "  $(GREEN)make clean$(NC)            - Полная очистка Docker и кэша"

# Сборка Docker-образов
build:
	@echo "$(GREEN)🔧 Сборка образов...$(NC)"
	$(DOCKER_COMPOSE) build

# Запуск контейнеров
up:
	@echo "$(GREEN)🚀 Запуск контейнеров...$(NC)"
	$(DOCKER_COMPOSE) up -d

# Автоперезапуск при изменениях
watch:
	@echo "$(YELLOW)👀 Наблюдение за файлами и автоматическая пересборка...$(NC)"
	$(DOCKER_COMPOSE) watch

# Остановка контейнеров
down:
	@echo "$(RED)⛔ Остановка контейнеров...$(NC)"
	$(DOCKER_COMPOSE) down

# Подключение к bash
shell:
	@echo "$(GREEN)💻 Подключение к контейнеру...$(NC)"
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) /bin/bash

# Очистка Docker и Python кэша
clean:
	@echo "$(RED)🧹 Полная очистка...$(NC)"
	$(DOCKER_COMPOSE) down -v --rmi all --remove-orphans
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
