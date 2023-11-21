const Kafka  = require('node-rdkafka');

const consumer = new Kafka.KafkaConsumer({
  'group.id': 'kafka',
  'metadata.broker.list': 'localhost:9092',
}, {});

consumer.connect();

consumer.on('ready', () => {
  console.log('consumer ready..')
  consumer.subscribe(['test']);
  consumer.consume();
}).on('data', (data) => {
    console.log('message received ',data.value.toString());
});