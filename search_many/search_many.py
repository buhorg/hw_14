from flask import Blueprint, render_template, redirect, request, url_for, current_app, jsonify

from DAO.movies import Movies

multi_search_blueprint = Blueprint('multi_search_blueprint', __name__, template_folder='templates')


@multi_search_blueprint.route('/multi_search/')
def search_start():
    return render_template('search_many.html')


@multi_search_blueprint.route('/multi_search/1/', methods=['POST'])
def search():
    gen = request.form.get('g')
    film_type = request.form.get('t')
    year = request.form.get('y')
    return redirect(url_for('.search_result', film_type=film_type, year=year, gen=gen))


@multi_search_blueprint.route('/multi_search/<film_type>/<year>/<gen>')
def search_result(film_type, year, gen):
    movies = Movies(current_app.config.get('PATH'))
    all_movies = movies.find_movies_by_type_year_genre(film_type, year, gen)
    return jsonify(all_movies)
