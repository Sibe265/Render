
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/aboutme")
def aboutme():
    return render_template("about_me.html")

if __name__ == '__main__':
    app.run(port="5001", use_reloader=True)

