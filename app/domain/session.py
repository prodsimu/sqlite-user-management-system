class Session:
    def __init__(self, id: int, user_id: int, created_at: str, active: bool) -> None:
        self.id = id
        self.user_id = user_id
        self.created_at = created_at
        self.active = active

    def __repr__(self):
        return (
            f"Session(id={self.id}, user_id={self.user_id}, "
            f"created_at='{self.created_at}', active='{self.active}')"
        )
