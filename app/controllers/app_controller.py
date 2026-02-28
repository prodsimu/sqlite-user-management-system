from app.services.user_service import UserService
from app.services.session_service import SessionService
from app.database.seeds import admin_seed
from app.domain.user_role import UserRole
from app.domain.user import User
from app.domain.session import Session


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
        self.running: bool = True

    # PUBLIC ENTRYPOINTS

    def start_app(self) -> None:
        self.bootstrap()

    def shutdown_system(self) -> None:
        self.runnig = False

    # INITIALIZATION

    def bootstrap(self) -> None:
        admin_seed(self.user_service)

        admin = self.user_service.get_user_by_username("admin")
        session = self.session_service.create_session(admin.id)

        self.current_user = admin
        self.current_session = session

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

    # MAIN LOOP

    def main_loop(self) -> None:
        while self.running:

            if not self.current_session:
                pass

            if self.current_user.role == UserRole.USER.value:
                pass

            if self.current_user.role == UserRole.ADMIN.value:
                pass
