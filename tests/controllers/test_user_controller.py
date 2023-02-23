from controllers.user_controller import UserController

from schemas.user import User


def test_create_user():
    # Arrange
    user = UserController.create_user(name="John Doe", phone_number="123-123-1234", address="123th Av")

    # Act
    created_user = User.select().where(User.id == user.id).get()

    # Assert
    assert user.id == created_user.id
    assert user.name == created_user.name
    assert user.phone_number == created_user.phone_number
    assert user.address == created_user.address

    # Delete test instances
    created_user.delete_instance()
