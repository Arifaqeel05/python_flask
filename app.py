# #improt Flask class from "flask" module
# from flask import Flask

# #create object of Flask class
# app= Flask(__name__)

# @app.route("/")
# def home():
#     return "<p> Hello Arif , Welcome to python development Journey</p>"

# @app.route('/aboutUs/') #if we tried to access "/aboutUs", no error
# def aboutUs():
#     return "<p>this is about page </p>"

# @app.route('/products') #if we tried to access '/products/', produce error
# def products():
#     return "<h1>PRODUCT PAGE</h1>" 

###

##this approch is not recommended , so we create the application factory
###__init__.py is the application factory