# FlaskBlog

You need pip and virtualenv to run this app.

1. pip
pip should be installed together with python 3 if you download it from python.org.
If you need to install pip, go to https://pip.pypa.io/en/latest/installing.html and follow the instructions for your operating system.

2. virtualenv

Install virtualenv with: pip install virtualenv


Running the app

1. Open the command line and navigate to the folder where the app's code lives.

2. Create a new virtual environment
From the command line, create a new isolated Python development environment by typing

virtualenv venv

3. Enter the isolated dev environment by typing

source venv/bin/activate

4. Install the app's dependencies

Dependencies are listed in a file called requirements.txt. Copy this file into the folder where the app's code lives. Then type:

$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev

pip install -r requirements.txt

This command will install the all app's dependencies.

5. App's database

Running the app will create a DB if it doesn't exist. If it doesn't work, you can create it manually using "python scripts/create_db.py".


7. Run the app
From the command line, type

python main.py

Go to http://localhost:5000/ in a browser to see the app.
