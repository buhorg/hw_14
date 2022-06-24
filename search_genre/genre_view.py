from flask import Blueprint, render_template, redirect, request, url_for, current_app, jsonify

import utils
from DAO.movies import Movies

genre_blueprint = Blueprint('genre_blueprint', __name__, template_folder='templates')


@genre_blueprint.route('/genre/')
def genre():
    return render_template('genre.html')


@genre_blueprint.route('/genre/1/', methods=['POST'])
def genre_():
    gen = request.form.get('g')
    return redirect(url_for('.genre_search', gen=gen))


@genre_blueprint.route('/genre/<gen>')
def genre_search(gen):
    movies = Movies(current_app.config.get('PATH'))
    all_movies = movies.find_movies_by_genre(gen)
    return jsonify(all_movies)
