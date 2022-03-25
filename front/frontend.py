from flask import Flask, request, jsonify, Response
import urllib.request
import urllib.parse
import json
import os

# azureIp = os.environ["azureIp"]
# azureIp = "http://" + azureIp + "/py/eval"
# pythonServiceHostName = ["http://p25sv/py/eval", azureIp]

app = Flask(__name__, static_url_path='')
# route_dir = 0
# bad_record = [0] * len(pythonServiceHostName)

@app.route("/")
def home2():
    return "Hello world! This is frontend."

@app.route("/front", methods=['POST'])
def receive():
    message = request.get_json()['message']
    print('received message from backend:', message)


@app.route("/response", methods=['POST'])
def response():
    resp = Response("I got it, roger")
    return resp

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6000)
