from flask import session
from passlib.hash import pbkdf2_sha256
from app.sdp_errors import AuthError

from injector import singleton, inject
from app.repository.UserRepository import UserRepository

@singleton
class AuthService:

    @inject
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def start_session(self, user):
        del user['password']
        session['authenticated_user'] = user
        return user

    def register(self, email: str, password: str):
        # Create the user object
        user = {
            "email": email,
            # Encrypt the password
            "password": pbkdf2_sha256.encrypt(password)
        }

        # Check for existing email address
        if self.repository.find_user_by_email(email):
            raise AuthError("Email address already in use")

        if self.repository.create_user(user) is None:
            raise AuthError("Failed to create new user")

        return self.start_session(user)

    def logout(self):
        session.clear()

    def login(self, email, password):

        user = self.repository.find_user_by_email(email)

        if user and pbkdf2_sha256.verify(password, user['password']):
            return self.start_session(user)

        raise AuthError("Invalid login credentials")

    @staticmethod
    def get_authenticated_user():
        if "authenticated_user" in session:
            return session["authenticated_user"]
        else:
            return None
