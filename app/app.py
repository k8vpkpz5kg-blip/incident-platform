from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from incident-platform"

@app.route("/health")
def health():
    return "ok"
