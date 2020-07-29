batch.seed_tickers: ## Populate Tickers
	docker-compose run --rm server python src/manage.py batch --data=seed_tickers

batch.seed_ohlc: batch.download_ohlc ## Populate OHLC Data
	./src/batch/seed/seed_ohlc.sh

batch.download_ohlc: ## Download OHLC Data
	docker-compose run --rm server python src/manage.py batch --data=download_ohlc