import sqlite3


class Movies:
    def __init__(self, PATH):
        self.path = PATH

    def connect_to_db(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
        return cursor

    def all_data(self):
        cursor = self.connect_to_db()
        sql_query = "SELECT * FROM netflix"
        cursor.execute(sql_query)
        return cursor.fetchall()

    def all_data_slice(self, my_limit, my_offset):
        cursor = self.connect_to_db()
        sql_query = "SELECT show_id, title FROM netflix LIMIT ? OFFSET ?"
        values = (my_limit, my_offset)
        cursor.execute(sql_query, values)
        return cursor.fetchall()

    def find_move_by_title(self, my_title):
        cursor = self.connect_to_db()
        sql_query = "SELECT title, country, listed_in, MAX(release_year), description FROM netflix WHERE title =?"
        cursor.execute(sql_query, (my_title,))
        return cursor.fetchone()

    def find_movies_by_rating(self, my_rating):
        cursor = self.connect_to_db()
        if my_rating == 'family':
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('G', 'PG', 'PG-13')"
        elif my_rating == 'children':
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('G')"
        else:
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('R', 'NC-17')"
        cursor.execute(sql_query)
        return cursor.fetchall()

    def find_movies_by_rating_slice(self, my_rating, my_limit, my_offset):
        cursor = self.connect_to_db()
        if my_rating == 'family':
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('G', 'PG', 'PG-13') LIMIT ? OFFSET ?"
        elif my_rating == 'children':
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('G') LIMIT ? OFFSET ?"
        else:
            sql_query = "SELECT rating, title, description  FROM netflix WHERE rating IN ('R', 'NC-17') LIMIT ? OFFSET ?"
        cursor.execute(sql_query, (my_limit, my_offset))
        return cursor.fetchall()

    def find_movies_by_years(self, year_start, year_end):
        cursor = self.connect_to_db()
        sql_query = "SELECT title, release_year FROM netflix WHERE release_year BETWEEN ? AND ?"
        years = (year_start, year_end)
        cursor.execute(sql_query, years)
        return cursor.fetchall()

    def find_movies_by_years_slice(self, year_start, year_end, my_limit, my_offset):
        cursor = self.connect_to_db()
        sql_query = "SELECT title, release_year FROM netflix WHERE release_year BETWEEN ? AND ? ORDER BY release_year DESC LIMIT ? OFFSET ?"
        values = (year_start, year_end, my_limit, my_offset)
        cursor.execute(sql_query, values)
        return cursor.fetchall()

    def find_movies_by_genre(self, genre):
        cursor = self.connect_to_db()
        sql_query = "SELECT title, description FROM netflix WHERE listed_in LIKE ? ORDER BY release_year DESC LIMIT 10"
        genre = '%' + genre + '%'
        cursor.execute(sql_query, (genre,))
        return cursor.fetchall()

    def find_movies_by_type_year_genre(self, film_type, year, genre):
        cursor = self.connect_to_db()
        sql_query = "SELECT title, description, netflix.release_year, netflix.type, listed_in FROM netflix WHERE listed_in LIKE ? AND netflix.type = ? AND release_year = ?"
        genre = '%' + genre + '%'
        values = (genre, film_type, year)
        cursor.execute(sql_query, values)
        return cursor.fetchall()

    def find_actors(self, actor1, actor2):
        cursor = self.connect_to_db()
        sql_query = "SELECT netflix.cast, COUNT(netflix.cast) as actors_count FROM netflix WHERE netflix.cast LIKE ? AND netflix.cast LIKE ? GROUP BY netflix.cast HAVING actors_count >0"
        values = ('%'+actor1+'%', '%'+actor2+'%')
        cursor.execute(sql_query, values)
        return cursor.fetchall()
