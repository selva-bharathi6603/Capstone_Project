from flask import Flask, render_template
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now()
    return render_template("index.html", hostname=hostname, time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
