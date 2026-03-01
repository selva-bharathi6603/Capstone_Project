from flask import Flask, render_template
import socket
import datetime
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now()
    return render_template("index.html", hostname=hostname, time=current_time)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/monitor")
def monitor():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return render_template("monitor.html", cpu=cpu, memory=memory)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
