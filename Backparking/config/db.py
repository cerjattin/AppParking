from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/dbpark'
user = "cerjattin"
password = "admin123"
direc = "cerjattin.mysql.pythonanywhere-services.com"
namebd = "cerjattin$dbpark"
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Movil12"

db = SQLAlchemy(app)
ma = Marshmallow(app)