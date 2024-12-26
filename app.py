from flask import Flask
app = Flask(__name__)


@app.route("/search")
def lw():
    return "Welcome to our App..."

app.run(host="0.0.0.0")

