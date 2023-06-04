def getMovieResponse(movie_details):
    movie = {
        'id':movie_details [0],
        'title': movie_details[1],
        'poster_path': movie_details[2],
        'language': movie_details[3],
        'overview': movie_details[4],
        'release_date': movie_details[5].strftime('%Y-%m-%d')
        
    }
    return movie