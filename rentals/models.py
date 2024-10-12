from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Reservation(db.Model):
    __tablename__ = 'Reservations'

    id = db.Column(db.Integer, primary_key=True)
    reserved_by = db.Column(db.String(100))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicles.id'))
    vehicle = db.relationship('Vehicle', backref=db.backref('Vehicles', uselist=False))

    pickup_date = db.Column(db.Date)
    return_date = db.Column(db.Date)

class Vehicle(db.Model):
    __tablename__ = 'Vehicles'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
