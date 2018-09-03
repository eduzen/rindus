help:
	@echo "help  -- print this help"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "ps    -- show status"
	@echo "clean -- clean all artifacts"
	@echo "test  -- run tests using docker"
	@echo "dockershell -- run bash inside docker"
	@echo "build -- rebuild rindus image"
	@echo "superuser -- runs createsuperuser"
	@echo "last-logs -- show tail of logs"
	@echo "shell_plus -- run django shell_plus inside docker"
	@echo "psql  -- run psql"

start:
	docker-compose up -d

last-logs:
	docker-compose logs -f --tail=10 rindus

stop:
	docker-compose stop

ps:
	docker-compose ps

clean: stop
	docker-compose rm --force -v

coverage:
	docker-compose run --rm rindus pytest --cov=.

only_test:
	docker-compose run --rm rindus pytest

pep8:
	docker-compose run --rm rindus flake8

test: pep8 only_test

dockershell:
	docker-compose run --rm rindus /bin/bash

migrations:
	docker-compose run --rm rindus python3 manage.py makemigrations

migrate:
	docker-compose run --rm rindus python3 manage.py migrate

superuser:
	docker-compose run --rm rindus python3 manage.py createsuperuser

shell_plus:
	docker-compose run --rm rindus python3 manage.py shell_plus

build:
	docker-compose build rindus

psql:
	docker-compose exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" postgres psql postgres postgres

.PHONY: help start stop ps clean test dockershell shell_plus only_test pep8 build last-logs psql superuser
