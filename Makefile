# Главный Makefile для habit_tracker_api

PROJECT_NAME = habit_tracker_api

# Цвета
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
NC = \033[0m

# Подключение docker/Makefile
include docker/Makefile

.PHONY: help dev migration migrate-local clean init

# Запуск FastAPI в dev-режиме
dev:
	@echo "$(GREEN)🚀 Запуск сервера разработки...$(NC)"
	uvicorn app.main:app --host localhost --port 8000 --reload

# Создание новой миграции
migration:
ifndef message
	$(error ❌ Укажите сообщение: make migration message="Initial commit")
endif
	alembic revision --autogenerate -m "$(message)"

# Применение миграций локально
migrate-local:
	alembic upgrade head

# Очистка pycache и docker-мусора
clean:
	@echo "$(RED)🧹 Очистка кеша и Docker...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	$(MAKE) docker-clean

# Быстрая инициализация проекта
init: docker-build docker-up docker-migrate docker-create-superuser
	@echo "$(GREEN)✅ Проект $(PROJECT_NAME) инициализирован$(NC)"

# Справка
help:
	@echo "$(GREEN)Makefile для проекта: $(PROJECT_NAME)$(NC)"
	@echo ""
	@echo "$(YELLOW)Основные команды (локальные):$(NC)"
	@echo "  $(GREEN)make dev$(NC)            - Запуск FastAPI в dev-режиме"
	@echo "  $(GREEN)make migration$(NC)      - Создать миграцию (требует message=\"...\")"
	@echo "  $(GREEN)make migrate-local$(NC)  - Применить миграции локально"
	@echo "  $(GREEN)make clean$(NC)          - Очистка кэша и Docker-контейнеров"
	@echo "  $(GREEN)make init$(NC)           - Быстрая инициализация проекта"
	@echo ""
	@echo "$(YELLOW)Docker команды:$(NC)"
	@$(MAKE) docker-help
