import unittest

from tests.rest.mock_app import create_app
from flask_testing import LiveServerTestCase


class TestBase(LiveServerTestCase):

    def create_app(self):
        return create_app()

    def test_app(self):
        self.assertEqual('test', 'test')


if __name__ == '__main__':
    unittest.main()
