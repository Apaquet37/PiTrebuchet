from flask import Flask, render_template, request
import math
app = Flask(__name__)
msg = ""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    return render_template("flaskFormTest.html", msg=msg)


app.run(port=80)
