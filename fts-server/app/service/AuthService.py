from typing import Optional

from flask import session
from injector import singleton, inject
from passlib.hash import pbkdf2_sha256

from app.model.AuthenticatedUser import AuthenticatedUser
from app.repository.AuthenticatedUserRepository import AuthenticatedUserRepository
from app.sdp_errors import AuthError


@singleton
class AuthService:

    @inject
    def __init__(self, repository: AuthenticatedUserRepository):
        self.repository = repository

    def update_session(self, user_dict: Optional[dict]=None) -> Optional[dict]:
        if user_dict is None and session["authenticated_user"]:
            user_dict = session["authenticated_user"]
        if user_dict is None:
            return

        # Confirm user is still valid (TODO: only after a time)
        user = self.repository.find_by_id(user_dict["id"])
        if user is None:
            self.logout()
            return None

        user_dict = user.to_dict()
        session['authenticated_user'] = user_dict
        user_dict["password"] = None
        return user_dict

    def register(self, email: str, password: str, login=True):
        # Create the user object
        user = AuthenticatedUser(
            email=email,
            # Encrypt the password
            password=pbkdf2_sha256.encrypt(password)
        )

        # Check for existing email address
        if self.repository.find_user_by_email(email):
            raise AuthError("Email address already in use")

        if self.repository.create_user(user) is None:
            raise AuthError("Failed to create new user")

        if login:
            return self.update_session(user.to_dict())
        else:
            return user.to_dict()

    @staticmethod
    def logout():
        session.clear()

    def login(self, email, password) -> dict:

        user = self.repository.find_user_by_email(email)

        if user and pbkdf2_sha256.verify(password, user.password):
            return self.update_session(user.to_dict())

        raise AuthError("Invalid login credentials")

    def get_authenticated_user(self) -> Optional[dict]:
        if "authenticated_user" in session:
            return self.update_session()
        else:
            return None
