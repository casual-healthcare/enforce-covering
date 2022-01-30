from flask import Flask, render_template, request
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/app", methods=["GET", "POST"])
def application():
    if request.method == "GET":
        return render_template("layout.html")
    else:
        print()