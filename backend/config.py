
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 


app = Flask(__name__) 
CORS(app)
# we can now send cross origin request 

# SQL Alchemy ORM means we can modify SQL actions in Python code only 
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mydatabase_reactflask.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)




