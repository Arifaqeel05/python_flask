from flask import Flask
import os
from . import db


##application factory
def create_app(test_config=None):
    app=Flask(__name__, instance_relative_config=True) #configuration files are relative to the “instance” folder, not the main project folder.
    #Set Default Configuration
    app.config.from_mapping( #sets configuration values directly.
        SECRETE_KEY='dev', #used by Flask for sessions and security. 'dev' is for development only
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #SQLite database file will be saved.
    )
    ##local configuration
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
        #It tries to load config.py from the instance folder (for example, instance/config.py).
        #silent=True means Flask won’t crash if the file doesn’t exist.
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    #Ensure Instance Folder Exists
    try:
        os.makedirs(app.instance_path) #Tries to create the instance folder if it doesn’t already exist.your project will create the SQLite database file there.
    except OSError:
        pass

    @app.route("/")
    def home():
        return "<h1> WELCOME TO THE HOME PAGE , THIS IS ARIF AQEEL AHMAD </h1>"

    @app.route('/about')
    def about():
        return "<h3> about us page </h3>"
    
    db.init_app(app)
    return app



