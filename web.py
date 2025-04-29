from flask import Flask, redirect, url_for, render_template
from InsulinOutline import *
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

pump_status = "Stopped"

@app.route("/")
def home():
    global pump_status
    return render_template("Login.html", status=pump_status)

@app.route("/status")

@app.route("/login")
def login():
    print("User logging in")
    return render_template("Login.html")

@app.route("/start", methods=["POST"])
def start():
    global pump_status
    pump_status = "Running"
    print("Pump Started!")
    start_thread()
    return redirect(url_for("home"))


@app.route("/stop", methods=["POST"])
def stop():
    global pump_status
    pump_status = "Stopped"
    print("Pump Stopped!")
    stop_pump()
    return redirect(url_for("home"))

@app.route("/view_result", methods=["POST"])
def results():
    print("View Results")
    with open("Results", "r") as f:
        data = f.read()
    return render_template("results.html", results=data)



if __name__ == "__main__":
    socketio.run(app, debug=True)
