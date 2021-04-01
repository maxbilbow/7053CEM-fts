from typing import Iterable, List

from injector import inject, singleton

from app.model.Skill import Skill
from app.repository.SkillRepository import SkillRepository


@singleton
class SkillService:
    @inject
    def __init__(self, repository: SkillRepository):
        self.__repository = repository

    def add_skill(self, display_name: str, aliases: List[str] = None):
        id = display_name.casefold()
        print(id)
        if self.find_by_id(id) is not None:
            raise Exception("Skill '{}' already exists".format(id))

        return self.__repository.insert(Skill(id=id, display_name=display_name, aliases=aliases))

    def find_by_id(self, id: str) -> dict:
        skill = self.__repository.find_by_id(id)
        return None if skill is None else skill.to_dict()

    def get_all(self) -> List[dict]:
        return list(gen(self.__repository.find_all()))


def gen(te_it: Iterable[Skill]):
    for o in te_it:
        yield o.to_dict()
