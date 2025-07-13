# Главный Makefile

# Название проекта (используется только для вывода)
PROJECT_NAME = habit_tracker_api

# Запуск в режиме разработки
dev:
	uvicorn app.main:app --host localhost --port 8000 --reload

# Запуск в продакшен режиме
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

# Очистка кеша
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Создание миграций
migration:
	alembic revision --autogenerate -m "$(message)"

# Применение миграций
migrate:
	alembic upgrade head

.PHONY: help
help:
	@echo "Makefile для проекта: $(PROJECT_NAME)"
	@echo ""
	@echo "🛠️  Docker:"
	@echo "  make build               - Сборка Docker-образов"
	@echo "  make up                  - Запуск контейнеров в фоне"
	@echo "  make start               - Запуск контейнеров в обычном режиме (с логами)"
	@echo "  make stop                - Остановка контейнеров"
	@echo "  make down                - Остановка и удаление контейнеров"
	@echo "  make restart             - Перезапуск контейнеров"
	@echo "  make logs                - Просмотр логов контейнеров"
	@echo "  make clean               - Полная очистка: контейнеры, образы, тома"
	@echo "  make shell               - Доступ к bash в контейнере web"
	@echo ""
	@echo "🐍 FastAPI:"
	@echo "  make dev                 - Запустить проект"
	@echo ""
	@echo "🚀 Быстрая инициализация проекта:"
	@echo "  make init                - Билд, запуск, создание суперпользователя и загрузка данных"
	@echo ""
	@echo "🌐 Nginx:"
	@echo "  make deploy-nginx        - Задеплоить конфигурацию Nginx"
	@echo "  make remove-nginx        - Удалить конфигурацию Nginx"
	@echo "  make check-nginx-config  - Проверить синтаксис конфигурации"
	@echo "  make clear-logs          - Очистить логи Nginx"
	@echo ""
	@echo "🔧 Утилиты:"
	@echo "  make help                - Показать эту справку"
