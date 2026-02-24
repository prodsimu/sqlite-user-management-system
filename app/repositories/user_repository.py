from app.database.connection import DatabaseConnection
from app.models.user import User


class UserRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    def create(self, name: str, username: str, password: str) -> User:
        cursor = self.connection.execute(
            """
            INSERT INTO users (name, username, password)
            VALUES (?, ?, ?)
            """,
            (name, username, password),
        )
        self.connection.commit()

        user_id = cursor.lastrowid
        return User(user_id, name, username, password)

    def find_by_username(self, username: str) -> User | None:
        cursor = self.connection.execute(
            """
            SELECT * FROM users WHERE username = ?
            """,
            (username,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return User(row["id"], row["name"], row["username"], row["password"])
