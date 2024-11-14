from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
import json
import os
from app.services.consumer_service.main_service import process_messages_all, process_hostage_message

load_dotenv(verbose=True)

app = Flask(__name__)


def consume_topic(topic: str, process_message_callback):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        process_message_callback(message.value)



if __name__ == '__main__':
    consume_topic(os.environ['KAFKA_TOPIC_MESSAGES_ALL'], process_messages_all)
    consume_topic(os.environ['KAFKA_TOPIC_MESSAGES_HOSTAGE'], process_hostage_message)
    consume_topic(os.environ['KAFKA_TOPIC_MESSAGES_EXPLOSIVE'], process_hostage_message)
    app.run()
