from extensions import db
from model import Favorites


def add_new_favorites(current_user, id):
    new_favorite = Favorites(
        user_id=current_user.id,
        bar_id=id,
    )
    db.session.add(new_favorite)
    db.session.commit()


def get_favorites_by(search, value):
    kwargs = {search: value}
    favorite = Favorites.query.filter_by(**kwargs).first()
    return favorite


def get_all_favorites_by(search, value):
    kwargs = {search: value}
    favorite = Favorites.query.filter_by(**kwargs).all()
    return favorite
