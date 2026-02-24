class User:
    def __init__(self, id: int, name: str, username: str, password: str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', username='{self.username}')"
