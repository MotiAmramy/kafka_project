from flask import Blueprint, request, jsonify
from app.repository.psql_repository.psql_read import get_user_data_by_email
from app.utils.convert_model_to_json import convert_user_model_to_json

user_Blueprint = Blueprint('user', __name__)



@user_Blueprint.route('/user', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        return (get_user_data_by_email(email)
                      .map(convert_user_model_to_json)
                     .map(lambda user: (jsonify(user), 200))
            .value_or(jsonify({"message": f"email {email} not found"}, 404))
            )


    except Exception as e:
        return jsonify({"error": str(e)}), 500
