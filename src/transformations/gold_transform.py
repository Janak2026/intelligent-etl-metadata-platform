"""
gold_transform.py
Aggregate Silver into Gold (business layer).
"""
from pyspark.sql import SparkSession

def build_gold(silver_path: str, gold_path: str):
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("delta").load(silver_path)
    # example: aggregated revenue per day
    df.createOrReplaceTempView("silver")
    gold_df = spark.sql("""
        SELECT to_date(order_date) as date, sum(amount) as total_revenue
        FROM silver
        GROUP BY to_date(order_date)
    """)
    gold_df.write.format("delta").mode("overwrite").save(gold_path)
    return gold_df
