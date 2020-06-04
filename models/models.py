from app import app as main
from flask_sqlalchemy import SQLAlchemy

main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/potholes.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)

# Class DataModel
# @arg Object
class Pothole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lat = db.Column(db.String(200))
    lngd = db.Column(db.String(200))
    description = db.Column(db.String(16777215))
