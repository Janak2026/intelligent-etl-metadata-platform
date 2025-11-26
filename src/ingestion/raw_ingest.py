"""
raw_ingest.py
Simple PySpark ingestion skeleton for reading CSV to Delta (local / Databricks).
"""
from pyspark.sql import SparkSession

def ingest_csv_to_delta(input_path: str, delta_path: str):
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.option("header", True).csv(input_path)
    df.write.format("delta").mode("overwrite").save(delta_path)
    return df

if __name__ == "__main__":
    # example paths (change in Databricks)
    ingest_csv_to_delta("/dbfs/FileStore/data/sample/orders.csv", "/tmp/delta/orders_raw")
