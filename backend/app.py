from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique=False, nullable=False)
    entry = db.Column(db.Text, nullable=False)

    def __init__(self, date, entry):
        self.date = date
        self.entry = entry


@app.route("/<text>", methods=["GET"])
def response(text):
    response = jsonify(message="Response: " + text)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/journal", methods=["POST"])
@cross_origin()
def journal():
    entry = request.get_json()
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.session.add(Journal(entry=entry, date=date))
    db.session.commit()
    return jsonify(message="POST request returned")

@app.route("/option", methods=["POST"])
@cross_origin()
def option():
    option = request.get_json()
    print(option)
    return jsonify(message="POST request returned")

@app.route("/questionnaire", methods=["POST"])
@cross_origin()
def questionnaire():
    answer = request.get_json()
    print(answer)
    return jsonify(message="POST request returned")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
