from flask import Blueprint, request, jsonify

from app.services.producer_service.producer import produce

messages_Blueprint = Blueprint('message', __name__)


@messages_Blueprint.route('/email', methods=['POST'])
def create_messages():
    try:
        message = request.json
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        produce(data=message, topic=os.environ['KAFKA_TOPIC_MEMBERSHIP_NEW'])
        return jsonify(member), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


