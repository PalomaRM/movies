from schemas.user import User


class UserController:

    @staticmethod
    def create_user(name: str, phone_number: str, address: str) -> User:
        user = User(name=name, phone_number=phone_number, address=address)
        user.save()
        return user
