### DATABASE
# ¯¯¯¯¯¯¯¯
database.bash: ## Connect to database to lauch commands
	docker-compose exec db bash

database.connect: ## Connect to database
	docker-compose exec db psql -Upostgres

database.migrate: ## Create alembic migration file
	docker-compose run --rm server python src/manage.py db migrate

database.upgrade: ## Upgrade to latest migration
	docker-compose run --rm server python src/manage.py db upgrade

database.downgrade: ## Downgrade latest migration
	docker-compose run --rm server python src/manage.py db downgrade
