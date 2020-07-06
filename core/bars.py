from werkzeug.exceptions import BadRequest

from external_ressource.geo_api_gouv import get_long_and_latitude
from model import Bars, db


def check_is_exist(bar):
    if not bar:
        raise BadRequest('No bar found!')


def add_new_bar(data):
    xyz = get_long_and_latitude(data['encoded_loc'])
    new_bar = Bars(
        name=data['name'],
        description=data['description'],
        openhour=data['openhour'],
        happyhour=data['happyhour'],
        adress=data['adress'],
        latitude=xyz.get("latitude"),
        longitude=xyz.get("longitude"),
    )
    db.session.add(new_bar)
    db.session.commit()


def get_a_bar(bar_id):
    bar = Bars.query.filter_by(id=bar_id).first()
    check_is_exist(bar)
    return bar


def get_all_bars():
    bars = Bars.query.all()
    return bars


def set_bar(id, data):
    bar = get_a_bar(id)
    bar.name = data['name']
    bar.openhour = data['openhour']
    bar.happyhour = data['happyhour']
    bar.description = data['description']
    db.session.commit()



