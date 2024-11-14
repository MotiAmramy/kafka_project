from app.db.models import User


def convert_user_model_to_json(user: User):
    user_data = {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'created_at': user.created_at,
        'ip_address': user.ip_address,
        'location': [{'id': loc.id, 'latitude': loc.latitude, 'longitude': loc.longitude, 'city': loc.city,
                      'country': loc.country} for loc in user.location],
        'devices': [{'id': device.id, 'device_id': device.device_id, 'browser': device.browser, 'os': device.os}
                    for device in user.device],
        'explosive_content': [{'id': explosive.id, 'sentence': explosive.sentence} for explosive in user.explosive_content],
        'hostage_content': [{'id': hostage.id, 'sentence': hostage.sentence} for hostage in user.hostage_content if
                            user.hostage_content is not None]
    }

    return user_data



def contains_suspicious_words(sentence):
    suspicious_keywords = ['hostage', 'explos', 'explosive']
    return any(keyword in sentence.lower() for keyword in suspicious_keywords)


def reorder_sentences(sentences):
    suspicious_sentences = [sentence for sentence in sentences if contains_suspicious_words(sentence)]
    safe_sentences = [sentence for sentence in sentences if not contains_suspicious_words(sentence)]
    return suspicious_sentences + safe_sentences