from flask import request
from flask_restplus import Namespace, Resource, fields

from apis.comun import token_required
from core.auth import check_is_admin, check_current_user
from core.bars import add_new_bar, get_a_bar, get_all_bars, set_bar
from model import db

api = Namespace('bars', description='Bars path')

bar_create_input = api.model(
    'Bar create input', {
        'name': fields.String(required=True, description='The bars name'),
        'description': fields.String(required=True, description='The bars description'),
        'adress': fields.String(required=True, description='The bars adress'),
        'encoded_loc': fields.String(required=True, description='The bars encoded localisation'),
    }
)

bar_update_input = api.model(
    'Bar update input', {
        'name': fields.String(required=True, description='The bars name'),
        'description': fields.String(required=True, description='The bars description'),
    }
)


@api.route('/')
class Bars(Resource):
    @api.doc(security='apikey', description="""
        <b>Get all Bars</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

            DESCRIPTION :

                Return all bars details from database.

            REQUEST :

                GET/bars/
    """)
    @token_required
    def get(self, current_user):
        bars = get_all_bars()
        output = []
        for bar in bars:
            bar_data = {'bar_id': bar.id,
                        'name': bar.name,
                        'description': bar.description,
                        'adress': bar.adress,
                        'latitude': bar.latitude,
                        'longitude': bar.longitude}
            output.append(bar_data)
        return {'bars': output}

    @api.doc(security='apikey', description="""
        <b>Registered a bar</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

            DESCRIPTION :

                Created a new bar in database.

            REQUEST :

                POST/bars/
                {
                    "name": "bar name"
                    "description": bar description"
                    "adress": "bar adress"
                    "encoded_loc": "bar encoded localisation"
                }
    """)
    @api.expect(bar_create_input)
    @token_required
    def post(self, current_user):
        data = request.get_json()
        add_new_bar(data)
        return {'message': 'New bar created!'}, 200


@api.route('/<int:id>')
class barsId(Resource):
    @api.doc(security='apikey', description="""
        <b>Get a specific bar</b></br></br>
        
            AUTHORIZATION :
            
                Requires an bar encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'
                
            DESCRIPTION :
                
                Return an bar from database (by id)
            
            REQUEST :
            
                GET/bars/{id}
    """)
    @token_required
    def get(self, current_user, id):
        bar = get_a_bar(id)
        bar_data = {'bar_id': bar.id,
                    'name': bar.name,
                    'description': bar.description,
                    'adress': bar.adress}
        return {'bar': bar_data}

    @api.doc(security='apikey', description="""
        <b>Change value of a specific bar</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

            DESCRIPTION :

                Update values of a specific bar (by id)

            REQUEST :

                PUT/bars/{id}
                {
                    "name": "bar name"
                    "description": bar description"
                }
    """)
    @token_required
    @api.expect(bar_update_input)
    def put(self, current_user, id):
        data = request.get_json()
        set_bar(id, data)
        return {'message': 'The bar has been update!'}

    @api.doc(security='apikey', description="""
        <b>Delete a specific bar</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin' 

            DESCRIPTION :

                Delete bar (by id)

            REQUEST :

                DELETE/bars/{id}
    """)
    @token_required
    def delete(self, current_user, id):
        check_is_admin(self)
        bar = get_a_bar(id)
        db.session.delete(bar)
        db.session.commit()
        return {'message': 'The bar has been deleted!'}
