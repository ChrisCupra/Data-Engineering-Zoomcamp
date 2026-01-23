
import pandas as pd
from sqlalchemy import create_engine


def run():
    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = '5432'
    pg_db = 'ny_taxi'

    year = 2025
    month = 11

    target_table = 'green_taxi_data'

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