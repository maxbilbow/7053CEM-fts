import logging
import time
from typing import List, Iterable

from injector import inject, singleton

from app.model.TrainingEvent import TrainingEvent
from app.model.User import User
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.service.AuthService import AuthService
from app.service.UserService import UserService

ONE_DAY_IN_MILLIS = 86400000


def now_millis():
    return int(round(time.time() * 1000))


@singleton
class TrainingEventService:
    @inject
    def __init__(self, repository: TrainingEventRepository, auth_service: AuthService, user_service: UserService):
        self.__repository = repository
        self.__auth_service = auth_service
        self.__user_service = user_service

    def get_all_for_current_user(self) -> list:
        """
        Returns a list of courses managed by the current user
        """
        training_manager_id = self.__auth_service.get_authenticated_user()["id"]
        course_list = self.__repository.find_many_by_props({"trainingManagerId": training_manager_id})
        return list(gen(course_list))

    def find_all_within_days(self, days: int = 7) -> List[dict]:
        """
         Returns all events not older than 1 week (default)
        """
        limit = now_millis() - days * ONE_DAY_IN_MILLIS
        results = self.__repository.find_within_days(days)
        return self.__prepare_list(results)

    def __prepare_list(self, results: Iterable[TrainingEvent]) -> List[dict]:
        if self.__auth_service.is_authenticated():
            user = self.__user_service.get_profile()
            return list(generate_with_relevance(results, user))
        else:
            return list(gen(results))

    def get_all(self) -> List[dict]:
        results = self.__repository.find_all()
        return self.__prepare_list(results)

    def find_by_id(self, id: str) -> dict:
        return self.__repository.find_by_id(id).to_dict()

    @staticmethod
    def get_relevance_score(te: TrainingEvent, user: User) -> float:
        score = float(0)
        interests_matched = len(set(te.outcomes) & set(user.interests))
        prerequisites_matched = len(set(te.prerequisites) & set(user.competencies))
        if len(te.prerequisites) > 0:
            percentage_missed = 1.0 - float(prerequisites_matched) / len(te.prerequisites)
            score -= percentage_missed
            logging.info("{} prerequisites missing".format(percentage_missed))

        if len(user.interests) > 0:
            percentage_found = float(interests_matched) / len(user.interests)
            logging.info("{} outcomes found".format(percentage_found))
            score += percentage_found

        logging.info("Relevance score of {} given".format(score))
        return score


def gen(te_it: Iterable[TrainingEvent]):
    for o in te_it:
        yield o.to_dict()


def generate_with_relevance(it: Iterable[TrainingEvent], user: User):
    for o in it:
        te = o.to_dict()
        te["relevance"] = TrainingEventService.get_relevance_score(o, user)
        yield te



