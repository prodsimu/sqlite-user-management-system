def test_user_repository_create(user_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    assert user.id == 1


def test_user_repository_find_by_id(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    user = user_repository.find_by_id(1)

    assert user.username == "ignatius123"
