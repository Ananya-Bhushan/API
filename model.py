import mysql.connector

class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def getMoviedata(self):
        # Connect to the MySQL database
        conn=mysql.connector.connect(host = '127.0.0.1', user = 'root', password = 'admin1234', database = 'API')
        cursor = conn.cursor()

        # Fetch movie data from the database based on the movie ID
        query = "SELECT movie_id,movie_name,poster_path,lang,overview,releasedate FROM movie WHERE movie_id = %s"
        cursor.execute(query, (self.movie_id,))
        movie_data = cursor.fetchone()

        # Close the database connection
        cursor.close()
        conn.close()

        return movie_data