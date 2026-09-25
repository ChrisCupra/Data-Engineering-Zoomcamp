# Run PostgreSQL on the network
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  --network host \
  --name pgdatabase \
  postgres:18

  docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -e PGADMIN_LISTEN_PORT=8085 \
  -v pgadmin_data:/var/lib/pgadmin \
  --network host \
  --name pgadmin \
  dpage/pgadmin4

# In another terminal, run pgAdmin on the same network
uv run python ingest_data.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_trips_2021_1 \
  --year=2021 \
  --month=1 \
  --chunksize=100000

  docker run -it \
  --network host \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=localhost \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips_2021_1 \
    --chunksize=100000