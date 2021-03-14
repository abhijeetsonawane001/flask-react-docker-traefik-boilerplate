from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)  # to check load balancer
    return jsonify({"hello": "world", "serverIP": IPAddr})


if __name__ == "__main__":
    app.run()