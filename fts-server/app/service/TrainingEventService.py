import logging
from typing import List, Iterable

from injector import inject, singleton

from app.model.TrainingEvent import TrainingEvent
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.service.AuthService import AuthService


@singleton
class TrainingEventService:
    @inject
    def __init__(self, repository: TrainingEventRepository, auth_service: AuthService):
        self.__repository = repository
        self.__auth_service = auth_service

    def get_all_for_current_user(self) -> list:
        user_id = self.__auth_service.get_authenticated_user()["id"]
        course_list = self.repository.get_by_user_id(user_id)
        course_id_list = list(map(lambda course: course["id"], course_list))
        return list(gen(self.__repository.find_with_id_list(course_id_list)))

    def get_all(self) -> List[dict]:
        te_list = self.__repository.find_all()
        logging.info(te_list)

        return list(gen(self.__repository.find_all()))

    def find_by_id(self, id: str) -> dict:
        return self.__repository.find_by_id(id).to_dict()



def gen(te_it: Iterable[TrainingEvent]):
    for o in te_it:
        yield o.to_dict()
