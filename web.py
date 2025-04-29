from flask import Flask, redirect, url_for, render_template, request
from InsulinOutline import *
from flask_socketio import SocketIO
from login import *

app = Flask(__name__)
socketio = SocketIO(app)

pump_status = "Stopped"
file = ""

@app.route("/")
def home():
    global pump_status
    return render_template("Login.html", status=pump_status)

@app.route("/status")

@app.route("/login", methods=["GET", "POST"])  # <-- ADD methods here
def login_page():
    print("User logging in")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        TrueorFalse, file_from_login = login(username, password)
        print(TrueorFalse)
        print(file_from_login)

        if(TrueorFalse):
            global file
            file = file_from_login
            return render_template("Design.html")
        else:
            return render_template("Login.html")

@app.route("/create_account", methods=["GET", "POST"])
def create_account_page():
    if request.method == "POST":
        new_username = request.form.get("new_username")
        new_password = request.form.get("new_password")
        print("New account info:", new_username, new_password)
        create_account(new_username, new_password)
        # Here you would save the account info, etc
        return redirect(url_for("home"))

    return render_template("create_account.html")

@app.route("/start", methods=["POST"])
def start():
    global pump_status
    pump_status = "Running"
    start_thread()
    return render_template("Design.html", status=pump_status)

@app.route("/stop", methods=["POST"])
def stop():
    global pump_status
    pump_status = "Stopped"
    stop_pump()
    return render_template("Design.html", status=pump_status)

@app.route("/view_result", methods=["POST"])
def results():
    global file
    with open(file, "r") as f:
        data = f.read()
    return render_template("results.html", results=data)

@app.route("/pump", methods=["GET"])
def pump_page():
    global pump_status
    return render_template("Design.html", status=pump_status)


if __name__ == "__main__":
    socketio.run(app, debug=True)
