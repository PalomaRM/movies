from peewee import SqliteDatabase

from schemas.movie import Movie
from schemas.ticket import Ticket
from schemas.user import User

db = SqliteDatabase('movies.db')
db.create_tables([User, Movie, Ticket])
