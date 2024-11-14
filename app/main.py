from flask import Flask
# from app.db.database_psql import init_db
from app.routes.uesr_controller import user_Blueprint
from routes.messages_controller import messages_Blueprint


app = Flask(__name__)
app.register_blueprint(blueprint=messages_Blueprint, url_prefix="/api")
app.register_blueprint(blueprint=user_Blueprint, url_prefix="/api")


if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
