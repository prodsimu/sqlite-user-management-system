def test_user_repository_create(user_repository):
    user = user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    assert user.id == 1


def test_user_repository_find_by_id(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    user = user_repository.find_by_id(1)

    assert user.username == "ignatius123"


def test_user_repository_find_by_username(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    user = user_repository.find_by_username("ignatius123")

    assert user.name == "ignatius"


def test_user_repository_list_all_users(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")
    user_repository.create("joseph", "joseph123", "hashed_password", "user")
    user_repository.create("peter", "peter123", "hashed_password", "user")

    users_list = user_repository.list_all_users()

    assert users_list[0].name == "ignatius"
    assert users_list[1].name == "joseph"
    assert users_list[2].name == "peter"


def test_user_repository_update_by_fields(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")
    user_repository.update_by_fields(user_id=1, name="joseph")

    user = user_repository.find_by_id(1)

    assert user.name == "joseph"


def test_user_repository_delete(user_repository):
    user_repository.create("ignatius", "ignatius123", "hashed_password", "user")

    user = user_repository.find_by_id(1)

    user_repository.delete(1)

    user = user_repository.find_by_id(1)

    assert user is None
