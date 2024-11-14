import os
from dotenv import load_dotenv
from app.services.producer_service.producer import produce



load_dotenv(verbose=True)



def contains_suspicious_words(sentence):
    suspicious_keywords = ['hostage', 'explos', 'explosive']
    return any(keyword in sentence.lower() for keyword in suspicious_keywords)


def reorder_sentences(sentences):
    suspicious_sentences = [sentence for sentence in sentences if contains_suspicious_words(sentence)]
    safe_sentences = [sentence for sentence in sentences if not contains_suspicious_words(sentence)]
    return suspicious_sentences + safe_sentences

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





