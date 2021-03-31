from __future__ import annotations

from typing import List

from app.model.AbstractEntity import AbstractEntity


class Skill(AbstractEntity):
    id: str
    display_name: str
    aliases: List[str]

    def __init__(self, id:str, display_name: str):
        self.id = id
        self.display_name = display_name
        self.aliases = list()

    @staticmethod
    def from_dict(d: dict) -> Skill:
        skill = Skill(id=d["id"], display_name=d["displayName"])
        if "aliases" in d:
            skill.aliases = d["aliases"]
        return skill

    def to_dict(self: Skill) -> dict:
        return dict(
            id=self.id,
            displayName=self.display_name,
            aliases=self.aliases
        )


if __name__ == "__main__":
    s = Skill.from_dict({"id": "a", "displayName": "b", "aliases": ["a", "b", "c"]})
    print(s.to_dict())
