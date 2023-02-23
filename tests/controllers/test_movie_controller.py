from datetime import datetime
from controllers.movie_controller import MovieController

from schemas.movie import Movie


def test_create_movie():
    # Arrange
    movie = MovieController.create_movie(name="Demo Movie", dt=datetime(2023, 2, 1, 10, 10, 0), room="1A")

    # Act
    created_movie = Movie.select().where(Movie.id == movie.id).get()

    # Assert
    assert movie.id == created_movie.id
    assert movie.name == created_movie.name
    assert movie.datetime == created_movie.datetime
    assert movie.room == created_movie.room

    # Delete test instances
    created_movie.delete_instance()
