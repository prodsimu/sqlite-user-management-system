import re

from app.services.user_service import UserService
from app.services.session_service import SessionService
from app.database.seeds import admin_seed


class AppController:
    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.user_service = user_service
        self.session_service = session_service
        self.current_user = None
        self.current_session = None

    def bootstrap(self) -> None:
        admin_seed(self.user_service)

        admin = self.user_service.get_user_by_username("admin")
        session = self.session_service.create_session(admin.id)

        self.current_user = admin
        self.current_session = session

    def start_app(self) -> None:
        self.bootstrap()

    def login(self, username: str, password: str) -> None:
        user = self.user_service.authenticate_user(username, password)
        session = self.session_service.create_session(user.id)

        self.current_user = user
        self.current_session = session
