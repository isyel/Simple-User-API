# Simple-User-API

**A simple user directory API using FLask, where a user can create an account, log in to their account and update their profile (basic details). Also, the user should be able to see a list of all the registered users and view their profile.**


## How To Use Postman API Documentation

**Using the import option**

Copy this collection link and import it in your Postman App

[Shared Collection Link Here](https://www.getpostman.com/collections/cc6cbf4646299f4c8ca6)


## Virtual Environment

**Create Virtual Environment**

run `py -m venv venv` in the root 

run `venv\Scripts\activate`

To Deactivate virtual environment

run `deactivate`

**Install Requirements**

run `pip install -r requirements.txt`

**Run the App**

`flask run`


## Using Databases

There are two Database type connection created, one for MySql another for Sqlite.

**For MySql**

Go to the .env file and change the database username, password and host link for the *MYSQL_SQLALCHEMY_DATABASE_URI* constant, and comment out *SQLITE_SQLALCHEMY_DATABASE_URI*
Create a database named *simple_users* in your MySql console

**For Sqlite**

Uncomment the line with *SQLITE_SQLALCHEMY_DATABASE_URI*, and comment out *MYSQL_SQLALCHEMY_DATABASE_URI*

**Creating table and Seeding Data**

Run the command `flask db_create` to create the user table

Run the command `flask db_seed` to seed some dummy data into the table

Run the command `flask db_drop` to drop database and table created

