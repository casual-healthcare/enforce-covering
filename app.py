from flask import Flask, render_template, request
import cv2

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
cam = cv2.VideoCapture(0)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/app", methods=["GET", "POST"])
def application():
    if request.method == "GET":
        return render_template("layout.html")
    else: 
        s, img = cam.read()
        cv2.imshow('this is you', img)