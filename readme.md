# Basic App setup and dependencies
Database Used: MYSQL
Locally the tools used to create a database and view its contents
MySQL Installer 8.0.29 

Server 
Product: MySQL Community Server - GPL 
Version: 8.0.29 
Connector 
Version: C++ 8.0.29

Database Info:
user_for_db: str = "root",
password_for_db: str = "root",
database_name: str = "book_list"

This can be overridden by inserting different values in the DatabaseInstacnes constructor in database.py

### ENV
-To create a virtual environment for the app go to the desired location via a terminal and type the following:
python -m venv :name_of_the_env:

if you are using VS-CODE like me, you should see next to your terminal location the name of your env in brackets,
if not, from the root folder go to .\:name_of_the_env\Scripts\activate

### DEPENDENCIES
-From the root of the project run the following command
pip install -r dependencies/requirements.txt

Have XAMP or WAMP running, to startup MYSQL and establish a connection

# Running the App
from the root of the project with the env activated run cli.py show, simple as that ;)

# About the App
OOP architecture utilized, singleton pattern implemented to simulate a connection with the database,
pip packages for CLI command annotations and custom table with custom colored messages
