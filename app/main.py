from flask import Flask
from routes.messages_controller import messages_Blueprint


app = Flask(__name__)
app.register_blueprint(blueprint=messages_Blueprint, url_prefix="/api")


if __name__ == '__main__':
    app.run(debug=True)
