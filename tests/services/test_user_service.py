from app.domain.user_role import UserRole


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
