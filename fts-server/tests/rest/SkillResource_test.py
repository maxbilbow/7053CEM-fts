import os
import unittest
from unittest import mock
from unittest.mock import MagicMock

from flask_testing import LiveServerTestCase
from injector import inject

from app.database.mongo import MongoDatabase
from app.rest.SkillResource import SkillResource
from mock_app import create_app

SKILL_LIST = [
    {"id": "skill-id", "displayName": "Skill Name", "aliases": ["bob"]}
]


@mock.patch.dict(os.environ)
class SkillResourceTest(LiveServerTestCase):

    @inject
    def __init__(self, skill_resource: SkillResource):
        super().__init__()
        print("INJECTING", skill_resource)
        self.skill_resource = skill_resource

    # @classmethod
    # def setUpClass(cls):
    #     cls.env_patcher = mock.patch.dict(os.environ, {"FLASK_ENV": "development"})
    #     cls.env_patcher.start()
    #     super().setUpClass()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     super().tearDownClass()
    #     cls.env_patcher.stop()

    def setUp(self):
        super().setUp()
        self.assertEqual(os.environ["FLASK_ENV"], "development")

    def test_env(self):
        self.assertEqual(os.environ["FLASK_ENV"], "development")

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_that_valid_review_returns_201(self):
        print(self.skill_resource)


if __name__ == '__main__':
    with mock.patch.dict(os.environ, {"FLASK_ENV": "development"}):
        MongoDatabase.__init__ = MagicMock()
        MongoDatabase.find_all = MagicMock(return_value=SKILL_LIST)
        # with mock.patch.dict(os.environ, {"FROBNICATION_COLOUR": get_mock_colour()}):
    unittest.main()
