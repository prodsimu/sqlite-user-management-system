from app.database.connection import DatabaseConnection
from app.domain.user import User


class UserRepository:

    def __init__(self, connection=None):
        self.connection = connection or DatabaseConnection().get_connection()

    # CREATE

    def create(self, name: str, username: str, password: str, role: str) -> User:
        cursor = self.connection.execute(
            """
            INSERT INTO users (name, username, password, role)
            VALUES (?, ?, ?, ?)
            """,
            (name, username, password, role),
        )
        self.connection.commit()

        user_id = cursor.lastrowid
        return User(user_id, name, username, password, role)

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

        return User(
            row["id"], row["name"], row["username"], row["password"], row["role"]
        )

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

        return User(
            row["id"], row["name"], row["username"], row["password"], row["role"]
        )

    def list_all_users(self) -> list[User]:
        cursor = self.connection.execute(
            """
        SELECT * FROM users;
        """
        )

        row = cursor.fetchall()

        user_list = []

        for u in row:
            user = User(
                u["id"],
                u["name"],
                u["username"],
                u["password"],
                u["role"],
            )

            user_list.append(user)

        return user_list

    # UPDATE

    def update_by_fields(
        self,
        user_id: int,
        name: str | None = None,
        username: str | None = None,
        password: str | None = None,
        role: str | None = None,
    ) -> bool:

        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)

        if username is not None:
            fields.append("username = ?")
            values.append(username)

        if password is not None:
            fields.append("password = ?")
            values.append(password)

        if role is not None:
            fields.append("role = ?")
            values.append(role)

        if not fields:
            return False

        values.append(user_id)

        query = f"""
            UPDATE users
            SET {', '.join(fields)}
            WHERE id = ?
        """

        cursor = self.connection.execute(query, tuple(values))
        self.connection.commit()

        return cursor.rowcount > 0

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
