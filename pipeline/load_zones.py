import pandas as pd
from sqlalchemy import create_engine

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')

df_zones = pd.read_csv(url)
df_zones.to_sql(name='zones', con=engine, if_exists='replace')

print(f"loaded {len(df_zones)} zones in the database.")