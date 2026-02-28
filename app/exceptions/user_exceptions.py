class UserAlreadyExistsError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class InvalidUserDataError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass
