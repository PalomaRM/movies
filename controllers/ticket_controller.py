from random import randint

from schemas.movie import Movie
from schemas.ticket import Ticket
from schemas.user import User


class TicketController:

    @staticmethod
    def buy_ticket(user: User, movie: Movie) -> Ticket:
        # TODO: Validate movie date, and stuff like that
        ticket = Ticket(user=user.id,
                        movie=movie.id,
                        qr=f"{movie.id}-{randint(10000, 99999)}",
                        status=True)
        ticket.save()
        return ticket

    @staticmethod
    def scan_ticket(ticket: Ticket) -> None:
        if not ticket.status:
            raise ValueError("Your ticket is expired.")

        ticket.status = False
        ticket.save()
