from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
import json
import os
from app.services.consumer_service.consumer_service import process_messages_all, process_suspicious_message

load_dotenv(verbose=True)

app = Flask(__name__)







def consume_topic(topics: list, process_message_callback):
    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print(message)
        process_message_callback(message)




def topic_callback(message):
    topic = message.topic
    if topic == os.environ['KAFKA_TOPIC_MESSAGES_ALL']:
        process_messages_all(message.value)
    elif topic == os.environ['KAFKA_TOPIC_MESSAGES_HOSTAGE']:
        process_suspicious_message(message.value)
    elif topic == os.environ['KAFKA_TOPIC_MESSAGES_EXPLOSIVE']:
        process_suspicious_message(message.value)
    else:
        print(f"Unknown topic: {topic}")






if __name__ == '__main__':
    topics = [
        os.environ['KAFKA_TOPIC_MESSAGES_ALL'],
        os.environ['KAFKA_TOPIC_MESSAGES_HOSTAGE'],
        os.environ['KAFKA_TOPIC_MESSAGES_EXPLOSIVE']
    ]

    consume_topic(topics, topic_callback)
    app.run(debug=True)
