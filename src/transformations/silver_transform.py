"""
silver_transform.py
Transforms raw delta into cleaned Silver layer.
"""
from pyspark.sql import DataFrame, SparkSession

def transform_to_silver(raw_delta_path: str, silver_path: str):
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("delta").load(raw_delta_path)
    # example cleaning: drop duplicates, cast columns
    df_clean = df.dropDuplicates(["order_id"])
    df_clean.write.format("delta").mode("overwrite").save(silver_path)
    return df_clean
