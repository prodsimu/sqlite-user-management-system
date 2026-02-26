from app.repositories.user_repository import UserRepository
from app.domain.user import User
from app.domain.user_role import UserRole
from app.services.password_service import PasswordService
from app.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    # CREATE

    def create_user(self, name: str, username: str, password: str) -> User:
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UserAlreadyExistsError("Username already exists.")

        hashed_password = PasswordService.hash_password(password)

        default_role = UserRole.USER.value

        return self.user_repository.create(
            name, username, hashed_password, default_role
        )

    # READ

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("User not found.")

        return user

    # UPDATE

    # DELETE

    def delete_user(self, user_id: int) -> None:
        deleted = self.user_repository.delete(user_id)

        if not deleted:
            raise UserNotFoundError("User not found.")

    # AUTH

    def authenticate_user(self, username: str, password: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("Invalid credentials.")

        if not PasswordService.verify_password(password, user.password):
            raise UserNotFoundError("Invalid credentials.")

        return user
