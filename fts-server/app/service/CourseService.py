from injector import inject, singleton

from app.repository.CourseRepository import CourseRepository
from app.service.AuthService import AuthService


@singleton
class CourseService:
    @inject
    def __init__(self, repository: CourseRepository):
        self.__repository = repository

    def get_all_for_current_user(self) -> list:
        user_id = AuthService.get_authenticated_user()["id"]
        course_list = self.repository.get_by_user_id(user_id)["courses"]
        course_id_list = list(map(lambda course: course["id"], course_list))
        return self.__repository.find_with_id_list(course_id_list)

    def get_all(self) -> list:
        return self.__repository.find_all()
