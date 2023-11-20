const Kafka  = require('node-rdkafka');

// import eventType from '../eventType.js';

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
    // console.log(data);
    console.log('message received ',data.value.toString());
    
//   console.log(`received message: ${eventType.fromBuffer(data.value)}`);
});