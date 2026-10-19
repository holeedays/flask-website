from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")

@app.route("/about")
def about() -> str:
    return render_template("about.html")

################## testing

@app.route("/test/index_with_base")
def index_with_base() -> str:
    return render_template("index_with_base.html")


