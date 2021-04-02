from injector import inject, singleton

from app.model.User import User
from app.repository.UserRepository import UserRepository
from app.service.AuthService import AuthService


@singleton
class UserService:
    __repository: UserRepository
    __auth_service: AuthService

    @inject
    def __init__(self, repository: UserRepository, auth_service: AuthService):
        self.__repository = repository
        self.__auth_service = auth_service

    def __get_profile(self) -> User:
        """
        Uses the auth service to determine the current user
        and pulls their profile from the database

        If, unlikely, there is user in the system then the session is cleared and an exception is thrown
        """
        user_id = self.__auth_service.get_authenticated_user()["id"]
        user = self.__repository.find_by_id(user_id)
        if user is None:
            self.__auth_service.logout()
            raise Exception("user not found")
        return user

    def get_profile(self) -> User:
        return self.__get_profile()

    def update_profile(self, user_profile: dict):
        """
        Rather than storing the JSON as-is (which could be corrupt)
        we convert to a structured obeject which is then sent to the repository layer

        :param user_profile:
        :return: update user response
        """
        user = self.__get_profile()
        user.email = user_profile["email"]
        user.name = user_profile["name"]
        user.interests = user_profile["interests"]
        user.competencies = user_profile["competencies"]
        return self.__repository.update(user)
