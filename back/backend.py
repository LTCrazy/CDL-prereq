from flask import Flask, request, jsonify, Response
import sys
import io
import traceback

app = Flask(__name__, static_url_path='')


@app.route("/")
def home():
    return "Hello world! This is backend."


@app.route("/hello", methods=['POST'])
def hello():
    result = jsonify({'message': "Hello world"})
    # resp = Response("ok")
    # resp.headers['Custom-Header'] = 'Awesome'
    return result, {"Content-Type"}


@app.route("/print", methods=['POST'])
def receive2():
    message = request.get_data()
    print('received message from frontend:', message)
    return message


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
