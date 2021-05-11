from flask import Flask, render_template, request
import math
app = Flask(__name__)
msg = "Not Submitted"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    return render_template("benjiFlaskTest.html", msg=msg)


app.run(port=80)
