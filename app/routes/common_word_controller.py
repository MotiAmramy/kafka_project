# from flask import Blueprint
#
# messages_Blueprint = Blueprint('common_word', __name__)
#
#
# @messages_Blueprint.route('/common_word', methods=['POST'])
# def create_messages():
#     try:
#
#         message = request.json
#         print(message)
#         if not request.is_json:
#             return jsonify({"error": "Request must be JSON"}), 400
#
#         route_to_kafka_suspicious_sentences(message)
#         return jsonify(message), 201
#
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
