from flask import request
from flask_restplus import Namespace, Resource, fields

from apis.comun import token_required
from core.drinks import add_new_drinks, get_drinks_by, get_all_drinks_by
from model import db

api = Namespace('drinks', description='The drinks bars')

drinks_create_input = api.model(
    'Drinks create input', {
        'name': fields.String(required=True, description='The drink name'),
        'description': fields.String(required=True, description='The drink description'),
    }
)


@api.route('/<int:id>')
class Drinks(Resource):
    @api.doc(security='apikey', description="""
            <b>Get all drinks from specific bar</b></br></br>

                AUTHORIZATION :

                    Requires an bar encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

                DESCRIPTION :

                    Return list of drinks from one bar

                REQUEST :

                    GET/drinks/{bar_id}
        """)
    @token_required
    def get(self, current_user, bar_id):
        drinks = get_all_drinks_by('bar_id', bar_id)
        output_drink = []
        for drink in drinks:
            drink_data = {'id': drink.id,
                          'name': drink.name,
                          'description': drink.description,
                          'bar_id': drink.bar_id}
            output_drink.append(drink_data)
        return {'drinks': output_drink}

    @api.doc(security='apikey', description="""
           <b>Add drinks for one bar</b></br></br>

               AUTHORIZATION :

                   Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

               DESCRIPTION :

                   Created a new drinks for a bar in database.

               REQUEST :

                   POST/drinks/{bar_id}
                {
                    "name": "drink name"
                    "description": "drink description"
                }
       """)
    @api.expect(drinks_create_input)
    @token_required
    def post(self, current_user, bar_id):
        data = request.get_json()
        add_new_drinks(data, bar_id)
        return {'message': 'New drinks added!'}, 200

    @api.doc(security='apikey', description="""
        <b>Delete a specific drinks</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin' 

            DESCRIPTION :

                Delete drink (by drink id)

            REQUEST :

                DELETE/drinks/{drink_id}
    """)
    @token_required
    def delete(self, current_user, drink_id):
        drink = get_drinks_by('id', drink_id)
        db.session.delete(drink)
        db.session.commit()
        return {'message': 'The drink has been deleted!'}