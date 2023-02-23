from datetime import datetime

from schemas.movie import Movie


class MovieController:

    @staticmethod
    def create_movie(name: str, dt: datetime, room: str) -> Movie:
        movie = Movie(name=name, datetime=dt, room=room)
        movie.save()
        return movie
