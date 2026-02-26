class User:
    def __init__(self, id: int, name: str, username: str, password: str, role: str):
        self.id: int = id
        self.name: str = name
        self.username: str = username
        self.password: str = password
        self.role: str = role

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', username='{self.username}', role='{self.role}')"
