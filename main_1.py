from flask import Flask
from markupsafe import escape

"""
To run a Flask file, there are two options:
Let's say we have a Python file, 'main.py', and in this file we have a Flask object app, i.e. app = Flask(__name__).
Then to run this Python Flask file:
Method 1
-> flask --app main_1 run --debug

Method 2
-> flask --app main_1 run

If I had added the line code 
app.run(debug=True)
Then we would have to run 'python file_name.py' in the terminal 
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h3>Hello, World! You're Looking Great</h3>"

@app.route("/<my_name>")
def name(my_name:str):
    return f"Hello, {escape(my_name)}"

@app.route('/user/id_')
def name2(id_):
    try:
        return f"Welcome, {id_}"
    except Exception as e:
        print("the error is:  ",e)
