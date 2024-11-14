from typing import Dict

from returns.maybe import Maybe

from app.db.models import User





def convert_user_model_to_json(user: Maybe[User]) -> Dict[str, str]:
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
