from database.base import db
from flask import jsonify
import random

# Class DataModel
# @arg Object
class Pothole(db.Model):
    # Table name
    __tablename__ = 'potholes'

    # Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    desc = db.Column(db.String(16777215))
    stat = db.Column(db.String(30))

    # Initialize
    def __init__(self, name, lat, lng, desc, stat):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.desc = desc
        self.stat = stat

    # Seed
    def seed(fake):
        pothole = Pothole(
            name = fake.name(),
            lat = random.uniform(10.412, 10.415),
            lng = random.uniform(-75.520, -75.490),
            desc = fake.address(),
            stat = random.choice(['reported', 'repairing', 'repaired'])
        )
        pothole.save()

    # Save
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Serialize
    def serialize(self):
        return jsonify(
            id = self.id,
            name = self.name,
            lat = self.lat,
            lng = self.lng,
            desc = self.desc,
            stat = self.stat)
