from app.database.migrations import create_tables
from app.repositories.user_repository import UserRepository


def start():
    create_tables()

    repo = UserRepository()

    user = repo.create("Inacio", "inacio123", "123")
    print("Created:", user)

    found = repo.find_by_username("inacio123")
    print("Found:", found)


if __name__ == "__main__":
    start()
