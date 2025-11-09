from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h3>Hello, World! You're Looking Great</h3>"

@app.route("/<my_name>")
def name(my_name:str):
    return f"Hello, {escape(my_name)}"

@app.route('/user/<int : id_>')
def name2(id_):
    try:
        return f"Welcome, {id_}"
    except Exception as e:
        print("the error is:  ",e)
