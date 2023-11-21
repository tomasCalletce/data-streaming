from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import os

# Set environment variable for Spark
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

# Initialize Spark Session
spark = SparkSession \
    .builder \
    .appName("KafkaToSparkStreaming") \
    .getOrCreate()

# Define a UDF to process messages
def process_message(message):
    return message.upper()

# Register UDF
process_message_udf = udf(process_message, StringType())

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
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Apply the UDF to the "value" column for processing
df = df.withColumn("processed_value", process_message_udf(col("value")))

# Write the stream to the console
query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Await termination
query.awaitTermination()