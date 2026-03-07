from app.domain.user import User
from app.domain.user_role import UserRole
from app.exceptions.user_exceptions import (
    InvalidPasswordError,
    InvalidUserDataError,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from app.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    # CREATE

    def create(self, name: str, username: str, password: str) -> User:
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UserAlreadyExistsError("Username already exists.")

        if not 8 <= len(password) <= 64:
            raise InvalidPasswordError(
                "Password must be between 8 and 64 characters long."
            )

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

    def get_user_by_id(self, user_id: int) -> User:
        user = self.user_repository.find_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found.")

        return user

    def only_admin_exists(self) -> bool:
        return self.user_repository.check_if_only_admin_exists()

    def list_all_users(self) -> list:
        return self.user_repository.list_all_users()

    # UPDATE

    def update_user(
        self,
        user_id: int,
        name: str | None = None,
        username: str | None = None,
        password: str | None = None,
        role: UserRole | None = None,
    ) -> bool:

        user = self.user_repository.find_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found.")

        if password is not None:
            if not 8 <= len(password) <= 64:
                raise ValueError("Password must be between 8 and 64 characters long.")
            password = PasswordService.hash_password(password)

        if role is not None:
            if role not in [role.value for role in UserRole]:
                raise InvalidUserDataError("Invalid role.")

            if user.role == role:
                raise InvalidUserDataError("New role is same as current.")

        return self.user_repository.update_by_fields(
            user_id=user_id,
            name=name,
            username=username,
            password=password,
            role=role,
        )

    def is_new_password_same_as_current(self, user_id: int, new_password: str) -> bool:

        user = self.get_user_by_id(user_id)

        return PasswordService.verify_password(new_password, user.password)

    # DELETE

    def delete_user(self, current_user_id: int, user_id: int) -> None:

        if current_user_id == user_id:
            raise PermissionError("You can't delete your own user")

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
