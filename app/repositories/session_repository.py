from datetime import datetime, timezone
from app.database.connection import DatabaseConnection
from app.domain.session import Session
from app.domain.session_active import SessionActive


class SessionRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    # CREATE

    def create(self, user_id: int) -> Session:

        created_at = datetime.now(timezone.utc).isoformat()
        active = SessionActive.ACTIVE.value

        cursor = self.connection.execute(
            """
            INSERT INTO sessions (user_id, created_at, active)
            VALUES (?, ?, ?)
            """,
            (user_id, created_at, active),
        )
        self.connection.commit()

        session_id = cursor.lastrowid
        return Session(session_id, user_id, created_at, active)

    # UPDATE

    def deactivate(self, session_id: int) -> bool:
        cursor = self.connection.execute(
            """
            UPDATE sessions
            SET active = ?
            WHERE id = ? AND active = ?
            """,
            (
                SessionActive.INACTIVE.value,
                session_id,
                SessionActive.ACTIVE.value,
            ),
        )

        self.connection.commit()

        return cursor.rowcount > 0
