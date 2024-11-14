import os
from dotenv import load_dotenv
from app.services.producer_service.producer import produce
from app.utils.order_sentences import reorder_sentences



load_dotenv(verbose=True)




def route_to_kafka_suspicious_sentences(json_data):

    produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_ALL'])
    print('inserted to mongo successfully')

    ordered_sentences = reorder_sentences(json_data['sentences'])
    first_sentence = ordered_sentences[0]
    if 'hostage' in first_sentence:
        json_data['sentences'] = ordered_sentences

        print(f"Routing to Kafka topic 'messages.hostage': {ordered_sentences}")

        produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_HOSTAGE'])
    elif 'explos' in first_sentence or 'explosive' in first_sentence:
        json_data['sentences'] = ordered_sentences

        print(f"Routing to Kafka topic 'messages.explosive': {ordered_sentences}")

        produce(data=json_data, topic=os.environ['KAFKA_TOPIC_MESSAGES_EXPLOSIVE'])





