from peewee import *

db = SqliteDatabase('movies.db')


class Movie(Model):
    name = CharField()
    datetime = DateTimeField()
    room = CharField()

    class Meta:
        database = db  # This model uses the "movies.db" database.
