import sys
from os.path import dirname, abspath, join
path = abspath(join(dirname(__file__), '..', '..', 'server'))
sys.path.append(path)

from flask_testing import LiveServerTestCase
from flask import Flask
import urllib2

class PoiReviewResourceTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_that_valid_review_returns_201(self):
        response = urllib2.urlopen(self.get_server_url())

if __name__ == '__main__':
    unittest.main()
