from flask_restplus import Api

from .hello import api as ns_hello
from .auth import api as ns_auth
from .bars import api as ns_bars
from .favorites import api as ns_favorites

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
api.add_namespace(ns_bars)
api.add_namespace(ns_favorites)
