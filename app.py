from flask import Flask, render_template

app = Flask(__name__, static_folder="dist/static", template_folder="dist", static_url_path="/static")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

@app.route("/increment/<int:count>")
def increment(count):
    print(count)
    return f"{count + 1}"