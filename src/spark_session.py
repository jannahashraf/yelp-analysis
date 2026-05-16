from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("Yelp Preprocessing Pipeline") \
        .master("local[*]") \
        .getOrCreate()