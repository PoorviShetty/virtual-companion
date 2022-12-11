from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/<text>", methods=["GET"])
def response(text):
    response = jsonify(message="Response: " + text)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/journal", methods=["POST"])
@cross_origin()
def journal():
    entry = request.get_json()
    print(entry)
    return jsonify(message="POST request returned")

@app.route("/option", methods=["POST"])
@cross_origin()
def option():
    option = request.get_json()
    print(option)
    return jsonify(message="POST request returned")


if __name__ == "__main__":
    app.run(debug=True)
