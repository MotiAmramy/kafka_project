from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
import json
import os

from app.services.consumer_service.consumer_repository.consumer_repository_mongo import insert_message

load_dotenv(verbose=True)

app = Flask(__name__)



def consume_topic(topic: str, process_message_callback):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        # print(message)
        process_message_callback(message.value)





def process_messages_all(value):
    insert_message(value)
    print(value)




def process_hostage_message(message):



def process_explosive_message(message):





if __name__ == '__main__':
    consume_topic(os.environ['KAFKA_TOPIC_MESSAGES_ALL'], process_messages_all)
    consume_topic(os.environ['BOOTSTRAP_SERVERS'], process_class_registration_message)
    consume_topic(os.environ['BOOTSTRAP_SERVERS'], process_equipment_audit_message)
    app.run(port=5001)
