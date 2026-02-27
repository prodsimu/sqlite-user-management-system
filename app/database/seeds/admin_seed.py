from app.domain.user import User
from app.services.user_service import UserService
from app.domain.user_role import UserRole


def admin_seed(user_service: UserService):
    if user_service.user_repository.find_by_username("admin"):
        return

    user_service.create_admin("Admin", "admin", "admin123")
