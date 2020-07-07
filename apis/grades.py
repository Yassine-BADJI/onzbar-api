from flask import request
from flask_restplus import Namespace, Resource, fields

from apis.comun import token_required
from core.grades import add_new_grades, get_grades_average

api = Namespace('grades', description='The bars grades')

grades_create_input = api.model(
    'Grades create input', {
        'evaluation': fields.Integer(required=True, description='The bars grades'),
    }
)


@api.route('/<int:id_bar>')
class Grades(Resource):
    @api.doc(security='apikey', description="""
            <b>Get grades from specific bar</b></br></br>

                AUTHORIZATION :

                    Requires an bar encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

                DESCRIPTION :

                    Return grades from one bar

                REQUEST :

                    GET/grades/{bar_id}
        """)
    @token_required
    def get(self, current_user, id_bar):
        avg = get_grades_average(id_bar)
        return {'avg':  str(round(avg, 2))}

    @api.doc(security='apikey', description="""
           <b>Add grades for one bar</b></br></br>

               AUTHORIZATION :

                   Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

               DESCRIPTION :

                   Add a new grades for a bar in database.

               REQUEST :

                   POST/grades/{bar_id}
                {
                    "evaluation": "evaluation"
                }
       """)
    @api.expect(grades_create_input)
    @token_required
    def post(self, current_user, id_bar):
        data = request.get_json()
        add_new_grades(self, data, id_bar)
        return {'message': 'New grades added!'}, 200
