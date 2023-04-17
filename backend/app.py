from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from eng_to_kan import translate
# from get_chat_response import response as rp
from text_summariser import summarise_text
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
    mood = db.Column(db.Text, nullable=False)

    def __init__(self, date, entry, mood):
        self.date = date
        self.entry = entry
        self.mood = mood


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

    # print(translate("I am good"))
    bot_resp = translate(text) if translate(text) != None else ""
    # bot_resp = text 
    if pos < neg:
        response = jsonify(message=[bot_resp], tone = detect_sentiment("sad"))
        pos = 5
        neg = 0
    else:
        response = jsonify(message=[bot_resp], tone = detect_sentiment("neutral"))
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/journal", methods=["POST"])
@cross_origin()
def journal():
    entry = request.get_json()['entry']
    mood = request.get_json()['mood']
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    db.session.add(Journal(entry=entry, mood=mood, date=date))
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
    options_to_points = {'Never' : 1, 'Sometimes' : 2, 'More than half the days' : 3, 'All the time' : 4}
    points = 0
    for responses in answer:
        print(options_to_points[responses[1]])
        points += options_to_points[responses[1]]

    if points < 13:
        msg = "You are facing significant levels of distress!\n\nPlease head over to https://www.nhs.uk/nhs-services/mental-health-services/get-urgent-help-for-mental-health/ for help!"
    elif points >= 13 and points < 26:
        msg = "You are facing moderate levels of distress! \n\nWe recommend follwing this resource https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/"
    else:
        msg = "You have a strong sense of well-being!"

    return jsonify(message = msg)

@app.route("/summarise", methods=["GET"])
@cross_origin()
def summarise():
    text = ' '.join(convo)
    return jsonify(message=["Sure, here is your auto-generated journal entry!", summarise_text(text)])


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    [RegexpTokenizer, WhitespaceTokenizer, laplace_smoothing] = dill.load(open('./models/sent_helpers.pkl', 'rb'))

    w_tokenizer = WhitespaceTokenizer()
    sent_params = dill.load(open('./models/sent_params.pkl', 'rb'))
    loaded_model = dill.load(open('./models/sentiment_model.pkl', 'rb'))

    app.run(debug=True)
