import argparse
import pandas as pd
import subprocess
from sqlalchemy import create_engine
import os

# https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz


def main():
    parser = argparse.ArgumentParser(
        description="Aplicación de consola que imprime argumentos"
    )
    parser.add_argument(
        "--url",
        default="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz",
        help="Url",
    )

    parser.add_argument(
        "--is_lookup",
        default=False,
        help="Define if the file is a lookup file or not",
    )

    args = parser.parse_args()

    filename = os.path.basename(args.url)
    subprocess.run(["wget", args.url])
    subprocess.run(["gzip", "-d", filename])

    filename = filename[:-3]
    print(f"URL: {args.url}")
    print(f"Archivo descomprimido: {filename}")

    engine = create_engine("postgresql://myuser:mypassword@pg-database:5432/mydatabase")
    engine.connect()

    if args.is_lookup:
        df = pd.read_csv(filename)
        df.to_sql("green_tripdata_lookup", engine, if_exists="replace", index=False)

    else:
        df_raw_iter = pd.read_csv(
            filename, iterator=True, chunksize=100000, low_memory=False
        )

        while True:
            try:
                df = next(df_raw_iter)
            except StopIteration:
                break

            df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
            df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])

            df.to_sql("green_tripdata_data", engine, if_exists="append", index=False)


if __name__ == "__main__":
    main()
