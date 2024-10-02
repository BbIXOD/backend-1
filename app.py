from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def healthcheck():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<p>Current time: {current_time}</p>"
