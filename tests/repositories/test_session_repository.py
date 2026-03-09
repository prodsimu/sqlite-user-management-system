from app.domain.session_active import SessionActive


def test_session_repository_create(user_repository, session_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    session = session_repository.create(user.id)

    assert session.id == 1
    assert session.user_id == 1
    assert session.active == SessionActive.ACTIVE.value


def test_session_repository_deactivate(user_repository, session_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    session = session_repository.create(user.id)
    session_repository.deactivate(session.id)

    session_inactive = session_repository.get_active_by_user(user.id)

    assert session_inactive is None


def test_session_repository_get_active_by_user(user_repository, session_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    session = session_repository.create(user.id)

    active_session = session_repository.get_active_by_user(user.id)

    assert active_session is not None
    assert active_session.id == session.id
    assert active_session.user_id == user.id
    assert active_session.active == SessionActive.ACTIVE.value
