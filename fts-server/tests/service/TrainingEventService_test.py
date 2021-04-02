import random
import sys
import time
from os.path import dirname, abspath, join

from app.model.TrainingEvent import TrainingEvent
from app.model.User import User
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.service.AuthService import AuthService
from app.service.TrainingEventService import TrainingEventService
from app.service.UserService import UserService
from tests.words import make_sentence, SKILLS

path = abspath(join(dirname(__file__), '..', '..', 'server'))
sys.path.append(path)

import unittest
from unittest.mock import MagicMock

ONE_DAY = 86400000
ONE_HALF_DAY = ONE_DAY / 2
ONE_WEEK = ONE_DAY * 7
now = int(round(time.time() * 1000))


def generate_random_courses(count: int):
    now = int(round(time.time() * 1000))
    ONE_DAY = 86400000

    for i in range(count):
        event = TrainingEvent(title=make_sentence(5))
        event.synopsis = make_sentence(30)
        event.start_time = now + ONE_DAY * random.randint(-7, 50)
        for i in range(random.randint(0, 3)):
            event.outcomes.append(random.choice(SKILLS))
        for i in range(random.randint(0, 3)):
            event.prerequisites.append(random.choice(SKILLS))

        event.outcomes = list(set(event.outcomes))
        event.prerequisites = list(set(event.prerequisites))
        event.training_manager_id = "manager_id"
        yield event


def mock_user():
    user = User()
    user.interests = ["i1", "i2"]
    user.competencies = ["c1", "c2"]
    return user


class TrainingEventServiceTestCase(unittest.TestCase):
    te_repo: TrainingEventRepository
    auth_service: AuthService
    user_service: UserService

    def setUp(self) -> None:
        self.te_repo: TrainingEventRepository = MagicMock()
        self.user_service = MagicMock()
        self.auth_service = MagicMock()
        self.unit = TrainingEventService(self.te_repo, self.auth_service, self.user_service)

    def test_that_get_all_returns_dicts(self):
        RESULT_COUNT = 10
        self.te_repo.find_all = MagicMock(return_value=generate_random_courses(RESULT_COUNT))
        result = self.unit.get_all()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), RESULT_COUNT)
        self.assertIsInstance(result[1], dict)

    def test_that_find_within_days_returns_dicts(self):
        RESULT_COUNT = 10
        self.te_repo.find_within_days = MagicMock(return_value=generate_random_courses(RESULT_COUNT))
        result = self.unit.find_all_within_days()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), RESULT_COUNT)
        self.assertIsInstance(result[1], dict)

    def test_that_when_logged_in_data_has_relevance(self):
        self.te_repo.find_within_days = MagicMock(return_value=generate_random_courses(1))
        self.auth_service.is_authenticated = MagicMock(return_value=True)
        self.user_service.get_profile = MagicMock(return_value=mock_user())
        result = self.unit.find_all_within_days()
        self.assertIsInstance(result[0]["relevance"], float)

    def test_that_when_not_logged_in_data_does_not_have_relevance(self):
        self.te_repo.find_within_days = MagicMock(return_value=generate_random_courses(1))
        self.auth_service.is_authenticated = MagicMock(return_value=False)
        self.user_service.get_profile = MagicMock(return_value=mock_user())
        result = self.unit.find_all_within_days()
        self.assertFalse("relevance" in result[0])

    def test_zero_prerequisites_and_interests_yields_zero_relevance(self):
        event = next(generate_random_courses(1))
        event.outcomes = event.prerequisites = []
        user = mock_user()
        user.interests = user.competencies = []
        score = TrainingEventService.get_relevance_score(event, user)
        self.assertEqual(score, float(0))

    def test_that_matching_interests_increase_relevance(self):
        event = next(generate_random_courses(1))
        event.prerequisites = []
        event.outcomes = ["i1"]
        user = mock_user()
        user.interests = ["i1", "i2"]
        user.competencies = []
        score = TrainingEventService.get_relevance_score(event, user)
        self.assertEqual(score, float(0.5))

    def test_that_missing_prerequisites_decrease_relevance(self):
        event = next(generate_random_courses(1))
        event.prerequisites = ["c1", "c2"]
        event.outcomes = []
        user = mock_user()
        user.interests = []
        user.competencies = ["c1"]
        score = TrainingEventService.get_relevance_score(event, user)
        self.assertEqual(score, float(-0.5))


if __name__ == '__main__':
    unittest.main()
