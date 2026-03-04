from app.database.seeds.admin_seed import admin_seed
from app.domain.session import Session
from app.domain.user import User
from app.domain.user_role import UserRole
from app.services.session_service import SessionService
from app.services.user_service import UserService


class AppController:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.user_service = user_service
        self.session_service = session_service
        self.current_user: User | None = None
        self.current_session: Session | None = None
        self._admin_seeded = False

    def bootstrap(self) -> None:
        admin_created = admin_seed(self.user_service)

        if admin_created:
            self._admin_seeded = True

    # AUTH ACTIONS

    def login(self, username: str, password: str) -> None:
        user = self.user_service.authenticate_user(username, password)
        session = self.session_service.create_session(user.id)

        self.current_user = user
        self.current_session = session

    def logout(self) -> None:
        if not self.current_session:
            return

        self.session_service.deactivate_session(self.current_session.id)

        self.current_session = None
        self.current_user = None

    # UPDATE USER

    def update_name(self, user_id, name) -> None:
        self.user_service.update_user(user_id=user_id, name=name)

    def update_username(self, user_id, username) -> None:
        self.user_service.update_user(user_id=user_id, username=username)

    def update_password(self, user_id, password) -> None:
        self.user_service.update_user(user_id=user_id, password=password)

    def update_role(self, user_id, role) -> None:
        self.user_service.update_user(user_id=user_id, role=role)

    # UTIL

    def was_admin_seeded(self) -> bool:
        return self._admin_seeded

    def has_active_session(self) -> bool:
        return self.current_session is not None

    def is_admin(self) -> bool:
        return (
            self.current_user is not None
            and self.current_user.role == UserRole.ADMIN.value
        )
