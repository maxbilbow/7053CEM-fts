import sys
from os.path import dirname, abspath, join

from app.model.User import User
from app.repository.UserRepository import UserRepository
from app.service.AuthService import AuthService
from app.service.UserService import UserService

path = abspath(join(dirname(__file__), '..', '..', 'server'))
sys.path.append(path)

import unittest
from unittest.mock import MagicMock

MOCK_ID = "mock_id"
MOCK_EMAIL = "mock_email"
MOCK_NAME = "mock_name"


def mock_user_dict() -> dict:
    return {"id": MOCK_ID, "name": MOCK_NAME, "email": MOCK_EMAIL, "interests": [], "competencies": []}


def mock_user():
    user = User()
    user.id = "mock_id"
    user.name = "Bill Paxton"
    user.email = "mock@mock.mock"
    return user


class UserServiceTestCase(unittest.TestCase):
    user_repo: UserRepository
    auth_service: AuthService
    unit: UserService

    def setUp(self) -> None:
        self.user_repo: UserRepository = MagicMock()
        self.user_repo.find_by_id = MagicMock(return_value=mock_user())
        self.auth_service = MagicMock()
        self.auth_service.get_authenticated_user = MagicMock(return_value=mock_user_dict())
        self.unit = UserService(self.user_repo, self.auth_service)

    def test_when_user_exists_then_get_profile_returns_user(self):
        self.auth_service.is_authenticated = MagicMock(return_value=True)
        result = self.unit.get_profile()
        self.assertIsInstance(result, User)

    def test_user_not_exits_then_exception_raised(self):
        self.auth_service.is_authenticated = MagicMock(return_value=False)
        self.assertRaises(Exception, lambda o: self.unit.get_profile())

    def test_when_updating_user_then_correct_data_stored(self):
        profile = mock_user_dict()
        # Return input so that we can check it
        self.user_repo.update = MagicMock(side_effect=lambda o: o)
        result = self.unit.update_profile(profile)
        self.assertIsInstance(result, User)


if __name__ == '__main__':
    unittest.main()
