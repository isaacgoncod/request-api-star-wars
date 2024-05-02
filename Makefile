.PHONY: up
up:
	@echo "--> Starting your docker infrastructure..."
	@docker compose up --force-recreate -d

.PHONY: ps
ps:
	@echo "--> Listing all containers available..."
	@docker compose ps

.PHONY: down
down:
	@echo "--> Shutting down all containers..."
	@docker compose down

.PHONY: restart
restart:
	@echo "--> Restarting all containers..."
	@docker compose down
	@docker compose up --force-recreate -d

.PHONY: build
build:
	@echo "--> Building new docker image without cache..."
	@docker compose build --no-cache

.PHONY: bash
bash:
	@docker compose exec -it app bash

.PHONY: run
run:
	@docker compose exec -it app python run.py

.PHONY: pytest
pytest:
	@docker compose exec -it app pytest -v -s

.PHONY: git
git:
	@docker compose exec -it app git

.PHONY: pylint-config
test:
	@docker compose exec -it app pylint --generate-rcfile > .pylintrc