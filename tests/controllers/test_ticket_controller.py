import pytest

from datetime import datetime
from controllers.movie_controller import MovieController
from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController

from schemas.ticket import Ticket


def test_buy_ticket():
    # Arrange
    user = UserController.create_user(name="John Doe", phone_number="123-123-1234", address="123th Av")
    movie = MovieController.create_movie(name="Demo Movie", dt=datetime(2023, 2, 1, 10, 10, 0), room="1A")
    ticket = TicketController.buy_ticket(user=user, movie=movie)

    # Act
    created_ticket = Ticket.select().where(Ticket.id == ticket.id).get()

    # Assert
    assert ticket.id == created_ticket.id
    assert ticket.user == created_ticket.user
    assert ticket.movie == created_ticket.movie
    assert ticket.qr == created_ticket.qr
    assert ticket.status == created_ticket.status

    # Delete test instances
    created_ticket.delete_instance()
    user.delete_instance()
    movie.delete_instance()


def test_scan_ticket():
    # Arrange
    user = UserController.create_user(name="John Doe", phone_number="123-123-1234", address="123th Av")
    movie = MovieController.create_movie(name="Demo Movie", dt=datetime(2023, 2, 1, 10, 10, 0), room="1A")
    ticket = TicketController.buy_ticket(user=user, movie=movie)

    # Act
    TicketController.scan_ticket(ticket=ticket)  # "Scans" ticket and changes its status
    updated_ticket = Ticket.select().where(Ticket.id == ticket.id).get()

    # Assert
    assert not updated_ticket.status

    # Delete test instances
    updated_ticket.delete_instance()
    user.delete_instance()
    movie.delete_instance()


def test_scan_ticket_fails_with_expired_ticket():
    # Arrange
    user = UserController.create_user(name="John Doe", phone_number="123-123-1234", address="123th Av")
    movie = MovieController.create_movie(name="Demo Movie", dt=datetime(2023, 2, 1, 10, 10, 0), room="1A")
    ticket = TicketController.buy_ticket(user=user, movie=movie)

    # Act
    TicketController.scan_ticket(ticket=ticket)  # "Scans" ticket and changes its status

    # Assert
    with pytest.raises(ValueError):
        TicketController.scan_ticket(ticket=ticket)  # Try to scan an expired ticket

    # Delete test instances
    ticket.delete_instance()
    user.delete_instance()
    movie.delete_instance()
