from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

spark = SparkSession \
    .builder \
    .appName("KafkaToSparkStreaming") \
    .getOrCreate()

# Define Kafka parameters
kafka_topic_name = "test"
kafka_bootstrap_servers = 'localhost:9092'  # Change if your Kafka server is on a different host or port

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .load()

# Select the "value" column and cast it to a string
df = df.selectExpr("CAST(key AS STRING)","CAST(value AS STRING)")

# Write the stream to the console
# # In production, you would write it to a sink (database, file system, etc.)
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()