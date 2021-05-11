from flask import Flask, render_template, request
app = Flask(__name__)
msg = "Not Submitted"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global msg
        msg = request.form["name"]
    return render_template("benjiFlaskTest.html", msg=msg)


app.run(port=80)
