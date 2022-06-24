from flask import render_template, Blueprint, current_app

import utils
from DAO.movies import Movies

movie_blueprint = Blueprint('movie_blueprint', __name__, template_folder='templates')


@movie_blueprint.route('/movie/<uid>')
def movie_page(uid):
    movies = Movies(current_app.config.get('PATH'))
    film = movies.find_move_by_title(uid)
    movie = utils.get_dict_from_tuple(('title', 'country', 'genre', 'release_year', 'description'), film)
    return render_template("movie.html", movie=movie)

