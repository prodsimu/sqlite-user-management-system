from app.domain.session_active import SessionActive


def test_session_service_create_session_new_user(user_service, session_service):
    user = user_service.create("Test User", "testuser", "password123")

    session = session_service.create_session(user.id)

    assert session.id is not None
    assert session.user_id == user.id
    assert session.active == SessionActive.ACTIVE.value
    assert session.created_at is not None
