from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.services.password_service import PasswordService
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

        hashed_password = PasswordService.hash_password(password)

        return self.user_repository.create(name, username, hashed_password)

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("User not found.")

        return user

    def authenticate_user(self, username: str, password: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("Invalid credentials.")

        if not PasswordService.verify_password(password, user.password):
            raise UserNotFoundError("Invalid credentials.")

        return user
