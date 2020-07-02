import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_KEY = 'thisissecretkeytest'
    SENDGRID_KEY = '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'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'onzbar_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://rbnyeloycqjuay' \
                              ':30c2fab0c969a756ce0661acf4123d026d92daf058cf2b08d33db2a0fad5646f@ec2-54-246-115-40.eu' \
                              '-west-1.compute.amazonaws.com:5432/dfapcr3i52hgra '


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
sg_key = Config.SENDGRID_KEY
