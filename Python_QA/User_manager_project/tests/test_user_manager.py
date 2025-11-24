import pytest
from src.main import UserManager, UserAlreadyExists, UserNotFound


@pytest.fixture
def manager():
    return UserManager()


def test_create_user_success(manager):
    assert manager.create_user("david", "david@example.com") is True
    assert manager.users["david"]["email"] == "david@example.com"


def test_create_user_duplicate(manager):
    manager.create_user("david", "david@example.com")
    with pytest.raises(UserAlreadyExists):
        manager.create_user("david", "david2@example.com")


def test_create_user_invalid_email(manager):
    with pytest.raises(ValueError):
        manager.create_user("david", "not-an-email")


def test_get_user_success(manager):
    manager.create_user("david", "david@example.com")
    user = manager.get_user("david")
    assert user == {"email": "david@example.com"}


def test_get_user_not_found(manager):
    with pytest.raises(UserNotFound):
        manager.get_user("ghost")


def test_delete_user_success(manager):
    manager.create_user("david", "david@example.com")
    assert manager.delete_user("david") is True
    assert "david" not in manager.users


def test_delete_user_not_found(manager):
    with pytest.raises(UserNotFound):
        manager.delete_user("ghost")


def test_update_email_success(manager):
    manager.create_user("david", "david@example.com")
    assert manager.update_email("david", "new@example.com") is True
    assert manager.users["david"]["email"] == "new@example.com"


def test_update_email_invalid(manager):
    manager.create_user("david", "david@example.com")
    with pytest.raises(ValueError):
        manager.update_email("david", "bad-email")


def test_update_email_user_not_found(manager):
    with pytest.raises(UserNotFound):
        manager.update_email("ghost", "valid@example.com")
