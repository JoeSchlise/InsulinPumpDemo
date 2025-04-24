from flask import Flask, redirect, url_for, render_template
from InsulinOutline import *

app = Flask(__name__)


@app.route("/")
def home():
    pump_status = "Stopped"
    return render_template("Design.html", status=pump_status)

@app.route("/status")

@app.route("/start", methods=["POST"])
def start():
    pump_status = "Running"
    print("Pump Started!")
    pump_running()
    return render_template("Design.html", status=pump_status)

@app.route("/stop", methods=["POST"])
def stop():
    pump_status = "Stopped"
    print("Pump Stopped!")
    stop_pump()
    return render_template("Design.html", status=pump_status)

if __name__ == "__main__":
    app.run(debug=True)
