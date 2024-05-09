from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask (__name__)

#CONFIGURACION Y CONEXION A LA BASE DE DATO

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/ejemplo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "planas1"

db = SQLAlchemy(app)

ma = Marshmallow(app)