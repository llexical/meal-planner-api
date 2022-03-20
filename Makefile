export HEROKU_APP_NAME := llexical-meal-planner-api
export PORT := 8000
export PROJECT_NAME := $(subst -,_,$(notdir $(CURDIR)))

.PHONY: dev-build
dev-build: ## Create the docker image for you dev environment
	docker-compose build

.PHONY: dev-run
dev-run: ## Run a local instance of pass
	docker-compose up

.PHONY: dev-stop ## Shutdown the running container and remove any intermediate images. Usfull for when you think the container is stopped but docker doesn’t
dev-stop:
	docker-compose down

.PHONY: dev-clean
dev-clean: ## Remove all the docker containers for this project
	docker-compose down --rmi local --volumes

.PHONY: dev-setup
dev-setup: ## Get the env vars from Heroku
	setup-scripts/secrets

.PHONY: dev-ssh
dev-ssh: ## Open a shell on the current running docker image of pass
	docker-compose exec $(PROJECT_NAME) bash

.PHONY: dev-shell
dev-shell: ## Creates a shell in the project container, does not connect to a running instance. Use dev-ssh for that.
	docker-compose run --rm $(PROJECT_NAME) bash

.PHONY: dev-createsuperuser
dev-createsuperuser: ## Make a user account for the current instance
	docker-compose exec $(PROJECT_NAME) python manage.py createsuperuser

.PHONY: dev-makemigrations
dev-makemigrations: ## Generates migration files for any outstanding model changes
	docker-compose exec $(PROJECT_NAME) python manage.py makemigrations

.PHONY: dev-migrate
dev-migrate: ## Run any outstanding DB migrations for the current instance of pass
	docker-compose exec $(PROJECT_NAME) python manage.py migrate

.PHONY: create-staging-db-dump
create-staging-db-dump: ## Create a DB dump on staging
		heroku pg:backups:capture --app $(HEROKU_APP_NAME)

.PHONY: download-staging-db-dump
download-staging-db-dump: ## Get a local copy of the DB dump created by create-staging-db-dump
	heroku pg:backups:download --app $(HEROKU_APP_NAME)

.PHONY: restore-staging-db-dump
restore-staging-db-dump: ## Import data into the local postgress instance
	docker-compose exec $(PROJECT_NAME) pg_restore --verbose --clean --no-acl --no-owner -d 'postgres://test:test@db:5432/test' latest.dump

.PHONY: generate-gcal-oauth-creds
generate-gcal-oauth-creds: ## Generate OAuth credentials env variable for Google API authentication.
	docker-compose exec $(PROJECT_NAME) python scripts/googleCalendarSetup.py

.PHONY: help
help: ## This message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help