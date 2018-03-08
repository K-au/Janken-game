from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

def janken():
    janken = ["グー", "チョキ", "パー"]
    return np.random.choice(janken)

@app.route("/")
def index():
    title = "ジャンケンゲーム"
    return render_template("index.html", title=title)

@app.route("/post", methods=["POST"])
def post():
    title = "ようこそジャンケンゲームへ"
    message = janken()
    return render_template("index.html", title=title, message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
