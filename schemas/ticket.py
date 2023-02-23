from peewee import *

from schemas.user import User
from schemas.movie import Movie

db = SqliteDatabase('movies.db')


class Ticket(Model):
    user = ForeignKeyField(User, backref='tickets')
    movie = ForeignKeyField(Movie, backref='tickets')
    qr = CharField()
    status = BooleanField()  # True is active

    class Meta:
        database = db  # This model uses the "movies.db" database.
