from io import BytesIO

from werkzeug.exceptions import BadRequest

from config import file_types
from external_ressource.bucket_s3 import upload_s3
from external_ressource.geo_api_gouv import get_long_and_latitude
from external_ressource.qr_code import create_qr_code
from model import Bars, db


def check_is_exist(bar):
    if not bar:
        raise BadRequest('No bar found!')


def add_new_bar(data, url_image):
    xyz = get_long_and_latitude(data['encoded_loc'])
    new_bar = Bars(
        name=data['name'],
        image=url_image,
        description=data['description'],
        avg=0,
        openhour=data['openhour'],
        happyhour=data['happyhour'],
        adress=data['adress'],
        latitude=xyz.get("latitude"),
        longitude=xyz.get("longitude"),
    )
    db.session.add(new_bar)
    db.session.commit()
    db.session.flush()
    db.session.refresh(new_bar)
    create_qr_code(new_bar.id)


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


def add_picture(data, image):
    # récuperer l'extension à partir du nom du fichier
    extension = image.filename.rsplit('.', 1)[1].lower()

    # create a file object of the image
    image_file = BytesIO()
    image.save(image_file)

    # definir le nom du fichier
    key_name = "test1" + extension

    # definir le type de fichier à partir de l'extension
    content_type = file_types[extension]

    # envoyer sur le bucket
    url_image = upload_s3(image_file, key_name, content_type)

    return url_image
