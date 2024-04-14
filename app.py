from flask import Flask, render_template
import json

app = Flask(__name__, static_folder="dist/static", template_folder="dist", static_url_path="/static")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

@app.route("/api/increment/<int:count>")
def increment(count):
    print(count)
    return f"{count + 1}"

@app.route("/api/solutions")
def solutions():
    return json.dumps([{name: 'a'}])

@app.route("/api/gpt/<string:question>")
def gpt():
    print(question)
    return json.dumps([{answer: 'this is a really good question'}])