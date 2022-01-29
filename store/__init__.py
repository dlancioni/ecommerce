from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the application
app = Flask(__name__,
            static_url_path="",
            static_folder="static",
            template_folder="templates")

# used to improve safety on csrf_token login for forms
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'  
    
# create database conectivity    
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/db.dat"
db = SQLAlchemy(app)

# enable routes (nothing works without this line)
from store import routes