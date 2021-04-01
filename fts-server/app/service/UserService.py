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
        user_id = self.__auth_service.get_authenticated_user()["id"]
        user = self.__repository.find_by_id(user_id)
        if user is None:
            self.__auth_service.logout()
            raise Exception("user not found")
        return user

    def get_profile(self) -> dict:
        return self.__get_profile().to_dict()

    def update_profile(self, user_profile: dict):
        user = self.__get_profile()
        user.email = user_profile["email"]
        user.name = user_profile["name"]
        user.interests = user_profile["interests"]
        user.competencies = user_profile["competencies"]
        return self.__repository.update(user)
