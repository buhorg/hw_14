from flask import Blueprint, render_template, current_app, request, url_for, redirect

from DAO.movies import Movies
from utils import get_page_counts, get_list_of_dict_from_tuple

year_blueprint = Blueprint('year_blueprint', __name__, template_folder='templates')


@year_blueprint.route('/search/', methods=['GET'])
def year_page():
    return render_template("year.html")


@year_blueprint.route('/search/', methods=['POST'])
def year_result_page():
    y1 = request.form.get('y1')
    y2 = request.form.get('y2')
    uid = 1
    return redirect(url_for('.year_result_page_slice', y1=y1, y2=y2, uid=1))


@year_blueprint.route('/search/<int:y1>/to/<int:y2>/<int:uid>')
def year_result_page_slice(y1, y2, uid):
    movies = Movies(current_app.config.get('PATH'))
    all_movies = movies.find_movies_by_years(y1, y2)
    movies_count = len(all_movies)
    page_count_list = get_page_counts(movies_count)
    all_movies_slice = movies.find_movies_by_years_slice(y1, y2, current_app.config.get('COUNT_ON_PAGE'), (uid-1)*current_app.config.get('COUNT_ON_PAGE'))
    films = get_list_of_dict_from_tuple(('title', 'release_year'), all_movies_slice)
    return render_template("year.html", y1=y1, y2=y2, movies_count=movies_count, page_count_list=page_count_list,
                           films=films)


