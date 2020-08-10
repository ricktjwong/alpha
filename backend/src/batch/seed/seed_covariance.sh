# cp file to docker container

docker-compose exec db rm -Rf /var/lib/postgresql/data/pg_data
docker cp ./data $(docker-compose ps -q db):var/lib/postgresql/data/pg_data

# run psql command
docker-compose exec db psql -U "postgres" -d postgres -c "\copy ticker_covariance from '/var/lib/postgresql/data/pg_data/covariance.csv' delimiter ',' CSV HEADER;"