from flask import request
from flask_restplus import Namespace, Resource, fields

from apis.comun import token_required
from core.auth import add_new_user, check_is_admin, get_a_user, get_all_users, user_login, check_current_user, set_user
from model import db

api = Namespace('users', description='User login authenfication')

user_create_input = api.model('User created input', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user name'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
    'age': fields.String(required=True, description='The user age'),
})

user_update_input = api.model('User update input', {
    'email': fields.String(required=True, description='The user email'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
    'age': fields.String(required=True, description='The user age'),
})


@api.route('/login')
class UsersLogin(Resource):
    @api.doc(description="""
        <b>User login</b></br></br>

            AUTHORIZATION :

                No restriction for use this endpoint

            DESCRIPTION :

                Authentication for a registered user, return a valid token

            REQUEST :

                GET/users/login/
    """)
    def get(self):
        return user_login()


@api.route('/')
class Users(Resource):
    @api.doc(security='apikey', description="""
        <b>Get all users</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:admin'

            DESCRIPTION :

                Return all user from database.

            REQUEST :

                GET/users/
    """)
    @token_required
    def get(self, current_user):
        check_is_admin(self)
        users = get_all_users()
        output = []
        for user in users:
            user_data = {'user_id': user.id,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'email': user.email,
                         'age': user.age,
                         'admin': user.admin}
            output.append(user_data)
        return {'users': output}

    @api.doc(description="""
        <b>Registered a user</b></br></br>

            AUTHORIZATION :

                No restriction for use this endpoint

            DESCRIPTION :

                Created a new user in database.

            REQUEST :

                POST/users/
                {
                    "email": "user email"
                    "password": "user password"
                    "first_name": "user first name"
                    "last_name": "user last name"
                    "age": "user age"
                }
    """)
    @api.expect(user_create_input)
    def post(self):
        data = request.get_json()
        add_new_user(data)
        return {'message': 'New user created!'}


@api.route('/<int:id>')
class UsersId(Resource):
    @api.doc(security='apikey', description="""
        <b>Get a specific user</b></br></br>
        
            AUTHORIZATION :
            
                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'
                
            DESCRIPTION :
                
                Return an user from database (by id)
                Careful you can just get your own information
            
            REQUEST :
            
                GET/users/{id}
    """)
    @token_required
    def get(self, current_user, id):
        check_current_user(self, id)
        user = get_a_user(id)
        user_data = {'user_id': user.id,
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'email': user.email,
                     'age': user.age,
                     'admin': user.admin}
        return {'user': user_data}

    @api.doc(security='apikey', description="""
        <b>Change value of a specific user</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

            DESCRIPTION :

                Update values of a specific user (by id)

            REQUEST :

                PUT/users/{id}
                {
                "email": "user email"
                "first_name": "user first name"
                "last_name": "user last name"
                "age": "user age"
                }
    """)
    @token_required
    @api.expect(user_update_input)
    def put(self, current_user, id):
        data = request.get_json()
        set_user(self, id, data)
        return {'message': 'The user has been update!'}

    @api.doc(security='apikey', description="""
        <b>Delete a specific user</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:admin'

            DESCRIPTION :

                Delete user (by id)

            REQUEST :

                DELETE/users/{id}
    """)
    @token_required
    def delete(self, current_user, id):
        check_is_admin(self)
        user = get_a_user(id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'The user has been deleted!'}


@api.route('/admin/<int:id>')
class UsersAdmin(Resource):
    @api.doc(security='apikey', description="""
        <b>Promote admin a specific user</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:admin'

            DESCRIPTION :

                Promote an user administrator (by id)

            REQUEST :

                PUT/users/{id}
    """)
    @token_required
    def put(self, current_user, id):
        check_is_admin(self)
        user = get_a_user(id)
        user.admin = True
        db.session.commit()
        return {'message': 'The user has been promoted!'}
