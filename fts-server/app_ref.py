import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} timess.\n'.format(count)


# # main.py
# # Import the Flask class. An instance of this class will be our WSGI application.
# from flask_injector import FlaskInjector
# from dependencies import configure
# from app.config import app
#
#
# # Setup Flask Injector, this has to happen AFTER routes are added
# FlaskInjector(app=app, modules=[configure])
#
# if __name__ == "__main__":
#     app.run()
