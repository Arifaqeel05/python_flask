import sqlite3
from datetime import datetime
import click
from flask import current_app, g

def get_db():
    if 'db' not in g: #bd is just variable name
        g.db= sqlite3.connect(
            #database file path
            current_app.config['DATABASE'], #gives access to the active Flask application instance.config -->is a dictionary containing all the app’s settings.DATABASE -->gets the value of the DATABASE key, which you defined in your factory
            #type detection mode
            detect_types=sqlite3.PARSE_DECLTYPES
            #This is an optional argument to sqlite3.connect().
            #It controls how SQLite converts data types between SQL and Python automatically.
        )
        g.db.row_factory=sqlite3.Row
        #It tells SQLite to return rows as special objects that:
        # Behave like both tuples and dictionaries.
        # You can access values by column name
        #without row factory , it will return the tuples

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    #If 'db' exists, it returns the database connection object and removes it from g.
    # If 'db' doesn’t exist, it returns None (because of the second argument).
    if db is not None:
        db.close()

###now we will write a function that will run sql command files and 
##This code is part of how Flask sets up and prepares your SQLite database before the app runs.


#initialize the database
def init_db():
    db=get_db()
    #open the file safely and close it afterward
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo("DATABASE INITIALZED SUCCESSFULLY!!")

sqlite3.register_converter(
    "timestamp",
    lambda v:datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)