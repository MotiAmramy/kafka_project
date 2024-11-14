from app.repository.mongo_repository.mongo_insertions import insert_message
from app.repository.psql_repository.psql_insertions import insert_user, insert_location, insert_device, \
    process_sentences


def insert_data_from_consumer(data):
    user = insert_user(data)
    insert_location(data, user.id)
    insert_device(data, user.id)
    process_sentences(data["sentences"], user.id)



def process_messages_all(value):
    insert_message(value)





def process_hostage_message(message):
    insert_data_from_consumer(message)
    print(message)



