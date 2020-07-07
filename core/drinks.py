from sqlalchemy import func

from core.bars import get_a_bar
from extensions import db
from model import Drinks


def add_new_drinks(data, bar_id):
    new_drink = Drinks(
        name=data['name'],
        price=data['price'],
        price_happyhour=data['price_happyhour'],
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


def get_price_average(bar_id):
    avg = db.session.query(func.avg(Drinks.price)).filter_by(bar_id=bar_id).first()
    return avg[0]


def update_avg_price(bar_id):
    avg = get_price_average(bar_id)
    bar = get_a_bar(bar_id)
    bar.avg = avg
    db.session.commit()
