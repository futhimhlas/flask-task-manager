import os
from flask import Flask # capitalisation NB here
if os.path.exists("env.py"): #  Here we import env package to use environment variables
    import env # we use an if statement as if we push to heroku, gitignore wont follow


app = Flask(__name__) # creating an instance of Flask


@app.route("/") # / refers to default root
def hello():
    return "Hello World ... again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True) # This should be false upon final deployment
        