from flask import Blueprint, request, jsonify
from app.services.producer_service.producer_service import route_to_kafka_suspicious_sentences




messages_Blueprint = Blueprint('message', __name__)


@messages_Blueprint.route('/email', methods=['POST'])
def create_messages():
    try:
        message = request.json
        print(message)
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400


        route_to_kafka_suspicious_sentences(message)
        return jsonify(message), 201


    except Exception as e:
        return jsonify({"error": str(e)}), 500


