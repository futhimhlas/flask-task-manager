# pip3 install flask
Sets us up to be able to import our flask functionality

# Storing confindential Variables
Use env.py and make sure it is gitignore
os.environ.setdefault("SECRET_KEY", "U9DJegKXHY")
1st argument is var name we use to get confidential data, second is the actual data itself

# pkill -9 python3 
To kill all instances of a running app

# pip3 freeze --local > requirements.txt
Creates txt file with requirements

# echo web: python app.py > Procfile
Heroku looks for procfile when running. echo cmd overrides this

# Heruko App Names
Dashes instead of spaces and lower case letters
env.py needs to remain hidden
its contents is then put in to settings and udner the config var section

# pip3 install flask-pymongo
In order to get flask to communicate with mongo

# pip3 install dnspython
TO use mongo SRV connection string

# requirements.txt 
needs to be updated after more packages are added

# routing 
is a string that when we attach it to a url, it will redirect to a particular function within our flask app

# Templates 
Flask looks for all HTML template files placed at with a directory at the root level
called templates
