#improt Flask class from "flask" module
from flask import Flask

#create object of Flask class
app= Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello Arif , Welcome to python development Journey</p>"

