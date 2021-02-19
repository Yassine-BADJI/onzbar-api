import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "thisisthelocalsecretkey")
    SENDGRID_KEY = os.environ.get("SENDGRID_KEY")
    # S3
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_HOST = "http://onzbar-s3.s3-website.eu-west-3.amazonaws.com"
    FILE_CONTENT_TYPES = {
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png'
    }


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
s3_bucket = Config.S3_BUCKET
s3_key = Config.S3_KEY
s3_secret = Config.S3_SECRET
s3_host = Config.S3_HOST
file_types = Config.FILE_CONTENT_TYPES
