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

# 
