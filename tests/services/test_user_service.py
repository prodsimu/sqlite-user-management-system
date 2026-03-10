from app.domain.user_role import UserRole
from app.exceptions.user_exceptions import (
    InvalidPasswordError,
    InvalidUserDataError,
    UserAlreadyExistsError,
    UserNotFoundError,
)


def test_user_service_create(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    assert user.id is not None
    assert user.name == "Ignatius"
    assert user.username == "ignatius123"
    assert user.role == UserRole.USER.value
    assert user.password != "password123"


def test_user_service_create_admin(user_service):
    admin = user_service.create_admin("Admin", "admin", "admin123")

    assert admin.id is not None
    assert admin.name == "Admin"
    assert admin.username == "admin"
    assert admin.role == UserRole.ADMIN.value
    assert admin.password != "admin123"


def test_user_service_get_user_by_username(user_service):
    user_service.create("Ignatius", "ignatius123", "password123")
    user = user_service.get_user_by_username("ignatius123")

    assert user is not None
    assert user.name == "Ignatius"
    assert user.username == "ignatius123"
    assert user.role == UserRole.USER.value


def test_user_service_get_user_by_id(user_service):
    created_user = user_service.create("Ignatius", "ignatius123", "password123")
    user = user_service.get_user_by_id(created_user.id)

    assert user is not None
    assert user.name == "Ignatius"
    assert user.username == "ignatius123"
    assert user.role == UserRole.USER.value


def test_user_service_list_all_users(user_service):
    user_service.create("Ignatius", "ignatius123", "password123")
    user_service.create_admin("Admin", "admin", "admin123")

    users = user_service.list_all_users()

    assert len(users) == 2
    assert users[0].username == "ignatius123"
    assert users[1].username == "admin"


def test_user_service_create_duplicate_username(user_service):
    user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.create("Another Ignatius", "ignatius123", "password456")
        assert False, "Expected UserAlreadyExistsError"
    except UserAlreadyExistsError as e:
        assert str(e) == "Username already exists."


def test_user_service_create_invalid_password(user_service):
    try:
        user_service.create("Ignatius", "ignatius123", "short")
        assert False, "Expected InvalidPasswordError"
    except InvalidPasswordError as e:
        assert str(e) == "Password must be between 8 and 64 characters long."


def test_user_service_get_nonexistent_user_by_username(user_service):
    try:
        user_service.get_user_by_username("nonexistent")
        assert False, "Expected UserNotFoundError"
    except UserNotFoundError as e:
        assert str(e) == "User not found."


def test_user_service_get_nonexistent_user_by_id(user_service):
    try:
        user_service.get_user_by_id(999)
        assert False, "Expected UserNotFoundError"
    except UserNotFoundError as e:
        assert str(e) == "User not found."


def test_user_service_update_user(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")
    updated = user_service.update_user(
        user_id=user.id,
        name="Ignatius Updated",
        username="ignatius_updated",
        password="newpassword123",
        role=UserRole.ADMIN,
    )

    assert updated is True

    updated_user = user_service.get_user_by_id(user.id)
    assert updated_user.name == "Ignatius Updated"
    assert updated_user.username == "ignatius_updated"
    assert updated_user.role == UserRole.ADMIN.value


def test_user_service_update_nonexistent_user(user_service):
    try:
        user_service.update_user(
            user_id=999,
            name="Nonexistent User",
            username="nonexistent",
            password="password123",
            role=UserRole.USER,
        )
        assert False, "Expected UserNotFoundError"
    except UserNotFoundError as e:
        assert str(e) == "User not found."


def test_user_service_update_user_duplicate_username(user_service):
    user1 = user_service.create("Ignatius", "ignatius123", "password123")
    user2 = user_service.create("Another User", "anotheruser", "password123")

    try:
        user_service.update_user(user_id=user2.id, username=user1.username)
        assert False, "Expected UserAlreadyExistsError"
    except UserAlreadyExistsError as e:
        assert str(e) == "Username already exists."


def test_user_service_update_user_invalid_password(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.update_user(user_id=user.id, password="short")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Password must be between 8 and 64 characters long."


def test_user_service_update_user_same_role(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.update_user(user_id=user.id, role=UserRole.USER.value)
        assert False, "Expected InvalidUserDataError"
    except InvalidUserDataError as e:
        assert str(e) == "New role is same as current."


def test_user_service_update_user_invalid_role(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.update_user(user_id=user.id, role="invalid_role")
        assert False, "Expected InvalidUserDataError"
    except InvalidUserDataError as e:
        assert str(e) == "Invalid role."


def test_user_service_update_user_own_role(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.update_user(
            user_id=user.id, current_user_id=user.id, role=UserRole.ADMIN.value
        )
        assert False, "Expected PermissionError"
    except PermissionError as e:
        assert str(e) == "You can't update your own role."


def test_user_service_is_new_password_same_as_current(user_service):
    user1 = user_service.create("Ignatius", "ignatius123", "password123")
    user2 = user_service.create("Joseph", "joseph123", "password123")

    assert user_service.is_new_password_same_as_current(user1.id, "password123") is True
    assert (
        user_service.is_new_password_same_as_current(user2.id, "password999") is False
    )


def test_user_service_delete_user(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")
    admin = user_service.create_admin("Admin", "admin", "admin123")

    user_service.delete_user(current_user_id=admin.id, user_id=user.id)

    try:
        user_service.get_user_by_id(user.id)
        assert False, "Expected UserNotFoundError"
    except UserNotFoundError:
        pass


def test_user_service_delete_own_user(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    try:
        user_service.delete_user(current_user_id=user.id, user_id=user.id)
        assert False, "Expected PermissionError"
    except PermissionError as e:
        assert str(e) == "You can't delete your own user"


def test_user_service_delete_nonexistent_user(user_service):
    admin = user_service.create_admin("Admin", "admin", "admin123")

    try:
        user_service.delete_user(current_user_id=admin.id, user_id=999)
        assert False, "Expected UserNotFoundError"
    except UserNotFoundError as e:
        assert str(e) == "User not found."


def test_user_service_authenticate_user_valid(user_service):
    user = user_service.create("Ignatius", "ignatius123", "password123")

    authenticated = user_service.authenticate_user("ignatius123", "password123")

    assert authenticated.id == user.id
    assert authenticated.username == user.username
