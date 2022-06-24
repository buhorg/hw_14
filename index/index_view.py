

from flask import render_template, Blueprint, current_app, request, jsonify

import utils
from DAO.movies import Movies
from utils import get_page_counts
from utils import get_list_of_dict_from_tuple

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.route('/', methods=['GET', 'POST'])
def index_page():
    movies = Movies(current_app.config.get('PATH'))
    all_movies = movies.all_data()
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.all_data_slice(current_app.config.get('COUNT_ON_PAGE'), 0)
    films = get_list_of_dict_from_tuple(('show_id', 'title'), all_movies_slice)
    return render_template("index.html", films=films, movies_count=movies_count, page_count_list=page_count_list)


@index_blueprint.route('/<int:uid>')
def index_page_slice(uid):
    movies = Movies(current_app.config.get('PATH'))
    all_movies = movies.all_data()
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.all_data_slice(current_app.config.get('COUNT_ON_PAGE'), (uid-1)*current_app.config.get('COUNT_ON_PAGE'))
    films = get_list_of_dict_from_tuple(('show_id', 'title'), all_movies_slice)
    return render_template("index.html", films=films, movies_count=movies_count, page_count_list=page_count_list)


@index_blueprint.route('/actors/')
def actors():
    actor_1 = request.args.get('a1')
    actor_2 = request.args.get('a2')
    movies = Movies(current_app.config.get('PATH'))
    actors = movies.find_actors(actor_1, actor_2)
    result = utils.find_actors_cowokers(actors, actor_1, actor_2, 2)
    return jsonify(result)
