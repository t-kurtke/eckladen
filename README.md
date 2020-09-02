# eckladen
My first django website :)

##Getting started
Prerequisites: Python 3 and pip installed

###Setup a virtual environment
`pip install virtual env\
cd /path/to/project/directory\
python3 -m venv env_name\
source env_name/bin/activate\
pip install -r requirements.txt`\

###Setup .env variables
In your project directory create a file called .env, open with text editor, enter this and save:

`django_secret_key = "<SECRET_KEY>" #replace <SECRET_KEY> with something like https://djecrety.ir/\
debug = "true"\
localhost = "true"`\

###Setup database
`python manage.py migrate`\

###Run!
`python manage.py runserver`\
open browser, got to 
http://127.0.0.1:8000/blog/
