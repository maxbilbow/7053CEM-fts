import os
from functools import wraps

from flask import session, redirect
from flask_api import status


# Decorators
def dev_only(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if os.environ.get('FLASK_ENV') == 'development':
            return f(*args, **kwargs)
        else:
            raise Exception("NOT ALLOWED")

    return wrap
