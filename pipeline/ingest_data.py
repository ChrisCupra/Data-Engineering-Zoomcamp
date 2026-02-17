
import pandas as pd
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database')
@click.option('--year', default=2025, type=int, help='Year for taxi data')
@click.option('--month', default=11, type=int, help='Month for taxi data')
@click.option('--target_table', default='green_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table):

    df = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet')

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    print(pd.io.sql.get_schema(df, name=target_table, con=engine))

    df.head(n=0).to_sql(
        name=target_table,
        con=engine,
        if_exists='replace'
    )

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )


if __name__ == '__main__':
    run()