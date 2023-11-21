const Kafka = require('node-rdkafka');
const axios = require('axios');

const stream = Kafka.Producer.createWriteStream({
  'metadata.broker.list': 'localhost:9092'
}, {}, {
  topic: 'test'
});

const NEWS_API_KEY = '10fb3fc6cd794d9085a56f42b506ab1b'; // Replace with your NewsAPI key
const NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + NEWS_API_KEY;

async function fetchNewsHeadline() {
  try {
    const response = await axios.get(NEWS_API_URL);
    const articles = response.data.articles;
    if (articles.length > 0) {
      return articles[0].title; 
    }
    return null;
  } catch (error) {
    console.error('Error fetching news:', error);
    return null;
  }
}

async function queueMessage() {
  const headline = await fetchNewsHeadline();
  if (headline) {
    const success = stream.write(Buffer.from(headline));
    if (success) {
      console.log('Message successfully written to stream:', headline);
    } else {
      console.log('Something went wrong..');
    }
  } else {
    console.log('No headline to send');
  }
}

setInterval(() => {
  queueMessage();
}, 3000);