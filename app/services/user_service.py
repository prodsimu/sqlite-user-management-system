from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, name: str, username: str, password: str) -> User:
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UserAlreadyExistsError("Username already exists.")

        return self.user_repository.create(name, username, password)

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("User not found.")

        return user
