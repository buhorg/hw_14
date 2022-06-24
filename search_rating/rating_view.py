from flask import Blueprint, render_template, request, url_for, redirect, current_app

from DAO.movies import Movies
from utils import get_page_counts, get_list_of_dict_from_tuple

rating_blueprint = Blueprint('rating_blueprint', __name__, template_folder='templates')


@rating_blueprint.route('/rating/')
def rating():
    return render_template('rating.html')


@rating_blueprint.route('/rating/1/')
def rating_result():
    rating_description = request.args.get('rating')
    if rating_description == "children":
        return redirect(url_for('.rating_children', uid=1))
    elif rating_description == "family":
        return redirect(url_for('.rating_family', uid=1))
    else:
        return redirect(url_for('.rating_adult', uid=1))


@rating_blueprint.route('/rating/children/<int:uid>')
def rating_children(uid):
    movies = Movies(current_app.config.get('PATH'))
    my_rating = ('G',)
    all_movies = movies.find_movies_by_rating('children')
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.find_movies_by_rating_slice('children', current_app.config.get('COUNT_ON_PAGE'),
                                                          (uid - 1) * current_app.config.get('COUNT_ON_PAGE'))
    films = get_list_of_dict_from_tuple(('rating', 'title', 'description'), all_movies_slice)
    return render_template("rating.html", movies_count=movies_count, page_count_list=page_count_list,
                           films=films, rating='children')


@rating_blueprint.route('/rating/family/<int:uid>')
def rating_family(uid):
    movies = Movies(current_app.config.get('PATH'))
    my_rating = ('G, PG, PG-13')
    all_movies = movies.find_movies_by_rating('family')
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.find_movies_by_rating_slice('family', current_app.config.get('COUNT_ON_PAGE'),
                                                          (uid - 1) * current_app.config.get('COUNT_ON_PAGE'))
    films = get_list_of_dict_from_tuple(('rating', 'title', 'description'), all_movies_slice)
    return render_template("rating.html", movies_count=movies_count, page_count_list=page_count_list,
                           films=films, rating='family')


@rating_blueprint.route('/rating/adult/<int:uid>')
def rating_adult(uid):
    movies = Movies(current_app.config.get('PATH'))
    my_rating = ('R, NC-17')
    all_movies = movies.find_movies_by_rating('adult')
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.find_movies_by_rating_slice('adult', current_app.config.get('COUNT_ON_PAGE'),
                                                          (uid - 1) * current_app.config.get('COUNT_ON_PAGE'))
    films = get_list_of_dict_from_tuple(('rating', 'title', 'description'), all_movies_slice)
    return render_template("rating.html", movies_count=movies_count, page_count_list=page_count_list,
                           films=films, rating='adult')

