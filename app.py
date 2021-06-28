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
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # if existing user is truthy, display message to user
            flash("Username already exists")
            return redirect(url_for("register"))
            # redirecting user back to same register function

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # above is else statement if no user is found
        # get is using our name attribute
        mongo.db.users.insert_one(register)
        # register dictionary

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")
# Creates register.html and assigns it its URL


@app.route("/login", methods=["GET", "POST"])
# This part of the function tells flask
# where our page is
def login():
    if request.method == "POST":
        # check if the usernames exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        # username in form method must match name
        # attribute

        if existing_user:
            # truthy
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            # ensures hashed password matches user input
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
            # username doesn't exist
            
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True) 
        # This should be false upon final deployment
