from __future__ import annotations
from flask import jsonify
from typing import List, Optional
from app.model.AbstractEntity import AbstractEntity
from app.model.Competency import Competency


class User(AbstractEntity):
    id: str
    email: str
    competencies: List[Competency]
    interests: List[str]

    def __init__(self):
        self.competencies = list()
        self.interests = list()

    @staticmethod
    def from_dict(d: dict) -> User:
        user = User()
        user.id = d["id"]
        user.email = d["email"]
        if "competencies" in d:
            user.competencies = map(lambda c: Competency.from_dict(c), d["competencies"])
        if "interests" in d:
            user.interests = d["interests"]
        return user

    @staticmethod
    def to_dict(self) -> dict:
        return dict(
            email=self.email,
            competencies=list(map(lambda c: c.to_dict(), self.competencies)),
            interests=self.interests
        )


if __name__ == "__main__":
    o = User.from_dict({"id": "abc", "email": "a", "interests": ["a", "b", "c"]})
    print(o.to_dict())
    o = User.from_dict({"id": "abc", "email": "a", "password": "bottom"})
    print(o.to_dict())

    o = User.from_dict(
        {"id": "abc", "email": "a", "interests": ["a"], "competencies": [{"skillId": "A", "level": "3"}]})
    print(o.to_dict())
