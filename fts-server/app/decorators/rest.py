import os
from functools import wraps

from flask import session, redirect
from flask_api import status


# Decorators
def dev_only_rest(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if os.environ.get('FLASK_ENV') == 'development':
            return f(*args, **kwargs)
        else:
            return "NOT ALLOWED", status.HTTP_403_FORBIDDEN

    return wrap


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login'), status.HTTP_307_TEMPORARY_REDIRECT

    return wrap


def login_required_post(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login'), status.HTTP_401_UNAUTHORIZED

    return wrap


# Decorators
def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap
