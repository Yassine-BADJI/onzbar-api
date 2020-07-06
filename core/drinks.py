from extensions import db
from model import Drinks


def add_new_drinks(data, bar_id):
    new_drink = Drinks(
        name=data['name'],
        description=data['description'],
        bar_id=bar_id,
    )
    db.session.add(new_drink)
    db.session.commit()


def get_drinks_by(search, value):
    kwargs = {search: value}
    drink = Drinks.query.filter_by(**kwargs).first()
    return drink


def get_all_drinks_by(search, value):
    kwargs = {search: value}
    drink = Drinks.query.filter_by(**kwargs).all()
    return drink
