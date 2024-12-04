# from crypt import methods
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://${DB_USER}:${DB_PASS}@${DB_HOST}:3306/${DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def home():
    return jsonify({
        "Message": "app up and running successfully"
    })

@app.route("/notes", methods=["GET"])
def get_notes():
    return get_all_notes()
    

@app.route("/notes", methods=["POST"])
def access():
    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
