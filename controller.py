from flask import Flask, jsonify
from model import Movie
from view import getMovieResponse

app = Flask(__name__)

class MovieController:
    def __init__(self):
        pass

    def retrieveMoviedetails(self, movie_id):
        movie = Movie(movie_id)
        movie_data = movie.getMoviedata()

        if movie_data:
            movie_response = getMovieResponse(movie_data)
            return jsonify(movie_response), 200
        else:
            return jsonify({'error': 'data not found'}), 404
        
@app.route('/v1/movie/<int:movie_id>', methods=['GET'])
def retrieveMoviedetails(movie_id):
    movie_controller = MovieController()
    return movie_controller.retrieveMoviedetails(movie_id)

if __name__ == '__main__':
    app.run()