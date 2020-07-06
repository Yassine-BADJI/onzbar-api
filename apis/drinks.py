from flask import request
from flask_restplus import Namespace, Resource, fields

from apis.comun import token_required
from core.drinks import add_new_drinks, get_drinks_by, get_all_drinks_by, update_avg_price
from model import db

api = Namespace('drinks', description='The drinks bars')

drinks_create_input = api.model(
    'Drinks create input', {
        'name': fields.String(required=True, description='The drink name'),
        'description': fields.String(required=True, description='The drink description'),
        'price': fields.String(required=True, description='The drink price'),
        'price_happyhour': fields.String(required=True, description='The drink happy hour price'),
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
    def get(self, current_user, id):
        drinks = get_all_drinks_by('bar_id', id)
        output_drink = []
        for drink in drinks:
            drink_data = {'id': drink.id,
                          'name': drink.name,
                          'price': drink.price,
                          'price_happyhour': drink.price_happyhour,
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
                    "price": "drink price"
                    "price_happyhour": "drink price happy hour"
                }
       """)
    @api.expect(drinks_create_input)
    @token_required
    def post(self, current_user, id):
        data = request.get_json()
        add_new_drinks(data, id)
        update_avg_price(id)
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
    def delete(self, current_user, id):
        drink = get_drinks_by('id', id)
        db.session.delete(drink)
        db.session.commit()
        return {'message': 'The drink has been deleted!'}
