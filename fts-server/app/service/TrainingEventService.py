import logging
from typing import List

from injector import inject, singleton

from app.model.AuthenticatedUser import AuthenticatedUser
from app.model.TrainingEvent import TrainingEvent
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.service.AuthService import AuthService


@singleton
class TrainingEventService:
    @inject
    def __init__(self, repository: TrainingEventRepository):
        self.__repository = repository

    def get_all_for_current_user(self) -> list:
        user_id = AuthService.get_authenticated_user()["id"]
        course_list = self.repository.get_by_user_id(user_id)
        course_id_list = list(map(lambda course: course["id"], course_list))
        return self.__repository.find_with_id_list(course_id_list)

    def get_all(self) -> List[dict]:
        te_list = self.__repository.find_all()
        logging.info(te_list)

        def gen(stuff):
            for o in stuff:
                yield TrainingEvent.to_dict(o)
        return list(gen(self.__repository.find_all()))

