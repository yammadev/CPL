from database.base import db
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

    # Initialize
    def __init__(self, name, lat, lng, desc):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.desc = desc

    # Seed
    def seed(fake):
        pothole = Pothole(
            name = fake.name(),
            lat = random.uniform(10.412, 10.415),
            lng = random.uniform(-75.520, -75.490),
            desc = fake.address()
        )
        pothole.save()

    # Save
    def save(self):
        db.session.add(self)
        db.session.commit()
