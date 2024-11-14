from flask import Blueprint, request, jsonify
from app.repository.psql_repository.psql_read import get_user_data_by_email
from app.utils.routes_utils import convert_user_model_to_json

user_Blueprint = Blueprint('user', __name__)



@user_Blueprint.route('/user', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        user_model = get_user_data_by_email(email)
        user_data = convert_user_model_to_json(user_model)

        if user_data is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
