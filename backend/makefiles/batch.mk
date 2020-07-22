batch.populate_tickers: ## Populate Tickers
	docker-compose run --rm server python src/manage.py seed --data=ticker