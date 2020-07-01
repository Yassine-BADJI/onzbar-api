from flask_restplus import Api

from .hello import api as ns_hello
from .auth import api as ns_auth

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    }
}

api = Api(
    title='OnzBar Api',
    version='0.1',
    description='Api for OnzBar front-end',
    authorizations=authorizations
)

api.add_namespace(ns_hello)
api.add_namespace(ns_auth)