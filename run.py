from flask import Flask

from index.index_view import index_blueprint
from movie.movie_view import movie_blueprint
from search_genre.genre_view import genre_blueprint
from search_many.search_many import multi_search_blueprint
from search_rating.rating_view import rating_blueprint
from search_years.year_view import year_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(index_blueprint)
app.register_blueprint(movie_blueprint)
app.register_blueprint(year_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)
app.register_blueprint(multi_search_blueprint)

if __name__ == '__main__':
    app.run()
