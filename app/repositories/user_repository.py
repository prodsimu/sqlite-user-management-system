from app.database.connection import DatabaseConnection
from app.models.user import User


class UserRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    # CREATE

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

    # READ

    def find_by_id(self, user_id: int) -> User | None:
        cursor = self.connection.execute(
            """
            SELECT * FROM users WHERE id = ?
            """,
            (user_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return User(row["id"], row["name"], row["username"], row["password"])

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

    # UPDATE

    # DELETE

    def delete(self, user_id: int) -> bool:
        cursor = self.connection.execute(
            """
            DELETE FROM users WHERE id = ?
            """,
            (user_id,),
        )

        self.connection.commit()

        return cursor.rowcount > 0
