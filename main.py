from app.database.migrations import create_tables
from app.services.user_service import UserService


def start():
    create_tables()

    service = UserService()

    try:
        user = service.create_user("Inacio", "inacio123", "123")
        print("User created:", user)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    start()
