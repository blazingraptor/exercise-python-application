from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "It's a Flask application running on POD!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)
