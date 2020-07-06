from flask_restplus import Namespace, Resource

from apis.comun import token_required
from core.favorites import get_favorites_by, add_new_favorites, get_all_favorites_by
from model import db

api = Namespace('favorites', description='Your favorites bars')


@api.route('/')
class Favorites(Resource):
    @api.doc(security='apikey', description="""
        <b>Get all favorites bar</b></br></br>

            AUTHORIZATION :

                Requires an bar encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

            DESCRIPTION :

                Return list of favorites user bars

            REQUEST :

                GET/favorites/
    """)
    @token_required
    def get(self, current_user):
        favorites = get_all_favorites_by('user_id', self.id)
        output_favorite = []
        for favorite in favorites:
            favorite_data = {'id': favorite.id,
                             'bar_id': favorite.bar_id}
            output_favorite.append(favorite_data)
        return {'favorites': output_favorite}


@api.route('/<int:bar_id>')
class FavoritesId(Resource):
    @api.doc(security='apikey', description="""
           <b>Add Favorites bar</b></br></br>

               AUTHORIZATION :

                   Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin'

               DESCRIPTION :

                   Created a new favorite bar in database.

               REQUEST :

                   POST/favorites/

       """)
    @token_required
    def post(self, current_user, bar_id):
        add_new_favorites(self, bar_id)
        return {'message': 'New favorites added!'}, 200

    @api.doc(security='apikey', description="""
        <b>Delete a specific favorite</b></br></br>

            AUTHORIZATION :

                Requires an user encoded token for use this endpoint in the scope : 'onzbar:user' or 'onzbar:admin' 

            DESCRIPTION :

                Delete favorite bar (by bar id)

            REQUEST :

                DELETE/favorites/
    """)
    @token_required
    def delete(self, current_user, bar_id):
        favorite = get_favorites_by('bar_id', bar_id)
        db.session.delete(favorite)
        db.session.commit()
        return {'message': 'The favorite has been deleted!'}
