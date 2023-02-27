from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from eng_to_kan import translate
# from get_chat_response import response as rp
import dill
import re
import math

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

pos = 5
neg = 0
convo = []

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
    convo.append(text)
    print(convo)
    # values = get_values_for_pred()
    # pred = predict(values[0], values[1], values[2], values[3], values[4], [text])
    pred = loaded_model(sent_params[0], sent_params[1], sent_params[2], sent_params[3], sent_params[4], [text])
    print(pred, pos, neg)

    if pred[0] == 1:
        pos += 1
    else:
        neg += 1

    def rp(x):
        return x
    
    bot_resp = rp(text) if rp(text) != None else ""

    if pos < neg:
        response = jsonify(message=[bot_resp], tone = detect_sentiment("sad"))
        pos = 0
        neg = 0
    else:
        response = jsonify(message=[bot_resp], tone = detect_sentiment("neutral"))
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/journal", methods=["POST"])
@cross_origin()
def journal():
    entry = request.get_json()
    convo.append(entry)
    print(convo)
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.session.add(Journal(entry=entry, date=date))
    db.session.commit()
    return jsonify(message="POST request returned")

@app.route("/option", methods=["POST"])
@cross_origin()
def option():
    option = request.get_json()
    convo.append(option)
    print(convo)
    if option == 'Write a journal entry':
        return jsonify(action="journal")
    if option == 'Get help':
        return jsonify(action='quiz')
    return jsonify(message="POST request returned")

@app.route("/questionnaire", methods=["POST"])
@cross_origin()
def questionnaire():
    answer = request.get_json()
    convo.append(answer)
    print(convo)
    print(answer)
    return jsonify(message="POST request returned")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    [RegexpTokenizer, WhitespaceTokenizer, laplace_smoothing] = dill.load(open('./models/sent_helpers.pkl', 'rb'))

    w_tokenizer = WhitespaceTokenizer()
    sent_params = dill.load(open('./models/sent_params.pkl', 'rb'))
    loaded_model = dill.load(open('./models/sentiment_model.pkl', 'rb'))

    app.run(debug=True)
