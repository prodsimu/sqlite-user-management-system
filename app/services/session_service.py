from app.repositories.session_repository import SessionRepository
from app.domain.session import Session


class SessionService:

    def __init__(self, session_repository: SessionRepository) -> None:
        self.session_repository: SessionRepository = session_repository

    def create_session(self, user_id: int) -> Session:
        active_session = self.session_repository.get_active_by_user(user_id)

        if active_session:
            self.session_repository.deactivate(active_session.id)

        return self.session_repository.create(user_id)
