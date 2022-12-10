from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_example():
    response = jsonify(message="Simple server is running")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/", methods=["POST"])
@cross_origin()
def post_example():
    return jsonify(message="POST request returned")


if __name__ == "__main__":
    app.run(debug=True)
