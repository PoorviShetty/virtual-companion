from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sentiment_analyser import predict, get_values_for_pred

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

pos = 5
neg = 0

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique=False, nullable=False)
    entry = db.Column(db.Text, nullable=False)

    def __init__(self, date, entry):
        self.date = date
        self.entry = entry


def detect_sentiment(message):
    if message == "sad":
        return "negative"
    else:
        return "neutral"


@app.route("/<text>", methods=["GET"])
def response(text):
    global pos
    global neg

    values = get_values_for_pred()
    pred = predict(values[0], values[1], values[2], values[3], values[4], [text])

    if pred[0] == 1:
        pos += 1
    else:
        neg += 1

    if pos < neg:
        response = jsonify(message="Response: " + text, tone = detect_sentiment("sad"))
        pos = 0
        neg = 0
    else:
        response = jsonify(message="Response: " + text, tone = detect_sentiment("neutral"))
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
    if option == 'Write a journal entry':
        return jsonify(action="journal")
    if option == 'Get help':
        return jsonify(action='quiz')
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
