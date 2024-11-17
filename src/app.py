from flask import Flask, abort, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    if cnt.value != 0:
        cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def set():
    form_content = request.form.to_dict()
    new_number = form_content.get('number')

    if new_number is None:
        abort(400)

    try:
        new_number = int(new_number)
    except ValueError:
        abort(400)

    cnt.value = new_number
    return redirect("/")

