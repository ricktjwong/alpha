batch.populate_symbols: ## Populate Symbols
	docker-compose run --rm server python src/manage.py seed --data=symbol