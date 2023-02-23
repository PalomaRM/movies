from datetime import datetime

from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController
from controllers.movie_controller import MovieController

from db import migrations

from schemas.movie import Movie
from schemas.ticket import Ticket
from schemas.user import User

movie1 = MovieController.create_movie("Avatar", datetime(2023, 2, 1, 10, 10, 0), "1A")
movie2 = MovieController.create_movie("Avatar 2", datetime(2023, 2, 1, 10, 10, 0), "2A")

user1 = UserController.create_user("John Doe", phone_number="123-456-7890", address="123th Av")
user2 = UserController.create_user("Jane Doe", phone_number="111-222-3333", address="45th Av")

for u in User.select():
    print(u.id, u.name, u.phone_number)

for m in Movie.select():
    print(m.id, m.name, m.datetime, m.room)

jane_ticket = TicketController.buy_ticket(user2, movie1)

for t in Ticket.select():
    print(t.id, t.user, t.movie, t.qr, t.status)

TicketController.scan_ticket(jane_ticket)

for t in Ticket.select():
    print(t.id, t.user, t.movie, t.qr, t.status)

try:
    TicketController.scan_ticket(jane_ticket)
except ValueError:
    print("Can't scan an expired ticket!")

# This deletes all rows
Ticket.delete().execute()
User.delete().execute()
Movie.delete().execute()
