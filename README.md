# Headline Data Streaming with Apache Spark and Kafka

Streaming News Title Sentiment Analisis

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Docker
- Apache Spark
- Python 

### Installing

Clone this repo into you machine and run in the root of the proyect: 

    npm i

#### Setting Up Kafka

1. **Start Kafka using Docker Compose**:

    ```bash
    docker-compose up
    ```

    This command starts Kafka and Zookeeper services as defined in your `docker-compose.yml` file.

2. **Create a Kafka Topic**:

    ```bash
    docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test
    ```

    This command creates a new Kafka topic named `test`.

### Running the Application

1. **Run the Spark Application**:

    ```bash
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 main.py
    ```

    This will be our consumer.


2. **Now to start the producer we run**: 

    ```bash
    node main.js
    ```

### Authors

- Esteban Bernal Correa
- Juan Camilo Salazar Uribe
- Tomas Calle Espinal
