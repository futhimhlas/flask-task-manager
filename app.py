import os
from flask import (
    Flask, flash, render_template, redirect, request,
    session, url_for) 
# capitalisation NB here
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Mongodb stores data in JSON like format BSON
from werkzeug.security import generate_password_hash, check_password_hash
# Allow us to use werkzeug security features
if os.path.exists("env.py"):
    #  Here we import env package to use environment variables
    import env 
    # we use an if statement as if we push to heroku,
    # gitignore wont follow


app = Flask(__name__) 
# creating an instance of Flask

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
# This sets up an instance of Pymongo

@app.route("/")
@app.route("/get_tasks")
# / refers to default root
def get_tasks():
    # function name should match route decorator
    tasks = mongo.db.tasks.find() 
    # our tasks collection from mongo db
    # finds all docs from tasks collection and then we pass
    # it thru to our render_template
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
# Creates register.html and assigns it its URL


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True) 
        # This should be false upon final deployment
