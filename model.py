from sqlalchemy import ForeignKey

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
    favorites = db.relationship('Favorites', backref='users')


class Bars(db.Model):
    """ Bars Model for storing bars details """
    __tablename__ = "Bars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    avg = db.Column(db.Float)
    adress = db.Column(db.String(150))
    latitude = db.Column(db.String(150))
    longitude = db.Column(db.String(150))
    favorites = db.relationship('Favorites', backref='bars')
    drinks = db.relationship('Drinks', backref='bars')


class Favorites(db.Model):
    """ Favorites Model for storing favorites user bars """
    __tablename__ = "Favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("Users.id"), nullable=False)
    bar_id = db.Column(db.Integer, ForeignKey("Bars.id"), nullable=False)


class Drinks(db.Model):
    """ Drinks Model for storing Drinks into the bars """
    __tablename__ = "Drinks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    price = db.Column(db.Float)
    bar_id = db.Column(db.Integer, ForeignKey("Bars.id"), nullable=False)

