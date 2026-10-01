import pickle
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


# 1. SQL injection: user input becomes part of the SQL query.
@app.route("/user")
def find_user():
    username = request.args.get("name", "")
    connection = sqlite3.connect(":memory:")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return str(connection.execute(query).fetchall())


# 2. Command injection: user input is executed through a shell.
@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    return subprocess.check_output(
        "ping -c 1 " + host,
        shell=True,
        text=True,
    )


# 3. Unsafe deserialization: untrusted data is loaded with pickle.
@app.route("/load", methods=["POST"])
def load_data():
    return str(pickle.loads(request.get_data()))


# 4. Code injection: user input is evaluated as Python code.
@app.route("/calculate")
def calculate():
    expression = request.args.get("expression", "")
    return str(eval(expression))
