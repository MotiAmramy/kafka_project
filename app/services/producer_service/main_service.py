import os
from dotenv import load_dotenv
from app.services.producer_service.producer import produce
from app.utils.routes_utils import reorder_sentences



load_dotenv(verbose=True)




def route_to_kafka_suspicious_sentences(json_data):
    produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_ALL'])
    print('inserted to mongo successfully')
    ordered_sentences = reorder_sentences(json_data['sentences'])
    if 'hostage' in ordered_sentences[0].lower():
        json_data['sentences'] = ordered_sentences
        print(f"Routing to Kafka topic 'messages.hostage': {ordered_sentences}")
        produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_HOSTAGE'])
    elif 'explos' in ordered_sentences[0].lower() or 'explosive' in ordered_sentences[0].lower():
        json_data['sentences'] = ordered_sentences
        print(f"Routing to Kafka topic 'messages.explosive': {ordered_sentences}")
        produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_EXPLOSIVE'])





