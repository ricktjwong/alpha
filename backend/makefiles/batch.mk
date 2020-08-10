batch.seed_all: batch.seed_tickers batch.seed_ohlc batch.seed_covariance ## Populate all data sequentially

batch.seed_tickers: ## Populate Tickers
	docker-compose run --rm server python src/manage.py batch --data=seed_tickers

batch.seed_covariance: batch.download_covariance ## Populate covariance
	./src/batch/seed/seed_covariance.sh

batch.seed_ohlc: batch.download_ohlc ## Populate OHLC Data
	./src/batch/seed/seed_ohlc.sh
	docker-compose run --rm server python src/manage.py batch --data=prune_tickers

batch.download_ohlc: ## Download OHLC Data
	docker-compose run --rm server python src/manage.py batch --data=download_ohlc

batch.download_covariance: ## Calculate and download covariance between ticker pairs
	docker-compose run --rm server python src/manage.py batch --data=download_covariance

batch.prune_tickers:
	docker-compose run --rm server python src/manage.py batch --data=prune_tickers