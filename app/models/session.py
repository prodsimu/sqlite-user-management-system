class Session:
    def __init__(self, id: int, user_id: int, created_at: str):
        self.id = id
        self.user_id = user_id
        self.created_at = created_at

    def __repr__(self):
        return f"Session(id={self.id}, user_id={self.user_id}, created_at='{self.created_at}')"
