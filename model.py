from extensions import db


class Users(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.String(50))
    admin = db.Column(db.Boolean, default=False)


class Bars(db.Model):
    """ Bars Model for storing bars details """
    __tablename__ = "Bars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    adress = db.Column(db.String(150))
    latitude = db.Column(db.String(150))
    longitude = db.Column(db.String(150))
