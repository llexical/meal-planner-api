# Meal Planner API
Django api for meal planner fe app

## Requirements
- Docker
- Heroku Cli

## Setup
- Update `export HEROKU_APP_NAME := llexical-meal-planner-api` in the Makefile to your own application.
- `make dev-setup` to pull in environment variables
- `make dev-build` to build the container
- `make dev-run` to run the containers
- quickrun: `make dev-setup dev-build dev-run`
NOTE: for help on other commands type `make help` or checkout the makefile yourself.