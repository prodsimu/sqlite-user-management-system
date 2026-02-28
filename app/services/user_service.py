from app.repositories.user_repository import UserRepository
from app.domain.user import User
from app.domain.user_role import UserRole
from app.services.password_service import PasswordService
from app.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
    InvalidUserDataError,
)


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

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

    def create_admin(self, name: str, username: str, password: str) -> User:
        hashed = PasswordService.hash_password(password)
        return self.user_repository.create(name, username, hashed, UserRole.ADMIN.value)

    # READ

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("User not found.")

        return user

    # UPDATE

    def change_user_role(
        self,
        current_user_id: int,
        target_user_id: int,
        new_role: str,
    ) -> None:

        current_user = self.user_repository.find_by_id(current_user_id)

        if not current_user:
            raise UserNotFoundError("Current user not found.")

        if current_user.role != UserRole.ADMIN.value:
            raise PermissionError("Only admins can change user roles.")

        if new_role not in [role.value for role in UserRole]:
            raise InvalidUserDataError("Invalid role.")

        updated = self.user_repository.update_by_fields(
            user_id=target_user_id,
            role=new_role,
        )

        if not updated:
            raise UserNotFoundError("Target user not found.")

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
