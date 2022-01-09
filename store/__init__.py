from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the application
app = Flask(__name__,
            static_url_path="",
            static_folder="web/static",
            template_folder="web/templates")
    
# create database conectivity    
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.dat"
db = SQLAlchemy(app)

# enable routes (nothing works without this line)
from store import routes