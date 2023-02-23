from peewee import *

db = SqliteDatabase('movies.db')


class User(Model):
    name = CharField()
    phone_number = CharField()
    address = CharField()

    class Meta:
        database = db  # This model uses the "movies.db" database.
