from __future__ import annotations
from enum import Enum

from app.model.Skill import Skill
from app.model.AbstractEntity import AbstractEntity

from typing import Union, Optional


class SkillLevel(Enum):
    NOVICE = 0
    INTERMEDIATE = 1
    ADVANCED = 2


class Competency(AbstractEntity):
    __skill_id: str
    skill: Optional[Skill, None]
    level: SkillLevel

    def __init__(self, skill: Union[Skill, str], level=SkillLevel.NOVICE):
        if isinstance(skill, str):
            self.__skill_id = skill
            self.skill = None
        elif skill:
            self.skill = skill
        self.level = level

    @property
    def skill_id(self):
        if self.skill is not None:
            return self.skill.id
        else:
            return self.__skill_id

    @staticmethod
    def from_dict(d: dict) -> Competency:
        skill: Union[Skill, str]
        if "skill" in d:
            skill = Skill.from_dict(d["skill"])
        else:
            skill = d["skillId"]
        return Competency(skill=skill, level=d["level"])

    @staticmethod
    def to_dict(self: Competency) -> dict:
        d = dict(skillId=self.skill_id, level=self.level)
        if self.skill:
            d["skill"] = Skill.to_dict(self.skill)
        return d


if __name__ == "__main__":
    o = Competency.from_dict({"skill": {"id": "s1", "displayName": "S1"}, "level": 1})
    print(Competency.to_dict(o))
    o = Competency.from_dict({"skillId": "s1id", "skill": {"id": "s1", "displayName": "S1"}, "level": 1})
    print(Competency.to_dict(o))
    o = Competency.from_dict({"skillId": "s1id", "level": 1})
    print(Competency.to_dict(o))
