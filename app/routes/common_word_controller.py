from flask import Blueprint, jsonify
from app.repository.psql_repository.psql_read import find_most_common_word

common_word_Blueprint = Blueprint('common_word', __name__)



@common_word_Blueprint.route('/common_word', methods=['GET'])
def get_common_word_in_sentences():
    try:
        data = find_most_common_word()

        if data is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
