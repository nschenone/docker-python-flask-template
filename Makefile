.PHONY: help

help:
	@echo "Usage:"
	@echo "    up:       Start app"
	@echo "    down:     Stop app"
	@echo "    restart:  Restart app"

up:
	docker-compose up -d --build

down:
	docker-compose down

restart: down up