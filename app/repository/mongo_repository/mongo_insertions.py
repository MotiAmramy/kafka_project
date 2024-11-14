from app.db.database_mongo import messages_collection

def insert_message(message):
    try:
        messages_collection.insert_one(message)
        return message
    except Exception as e:
        print(f"An error occurred while inserting the message: {e}")
        return None