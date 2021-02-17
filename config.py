import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "thisisthelocalsecretkey")
    SENDGRID_KEY = os.environ.get("SENDGRID_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'onzbar_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
sg_key = Config.SENDGRID_KEY
