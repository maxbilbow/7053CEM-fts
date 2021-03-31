from __future__ import annotations
from flask import jsonify
from typing import List, Optional
from app.model.AbstractEntity import AbstractEntity


class User(AbstractEntity):
    id: str
    email: str
    name: str
    competencies: List[str]
    interests: List[str]

    def __init__(self):
        self.name = ""
        self.competencies = list()
        self.interests = list()

    @staticmethod
    def from_dict(d: dict) -> User:
        user = User()
        user.id = d["id"]
        user.email = d["email"]
        if "name" in d:
            user.name = d["name"]
        if "competencies" in d:
            user.competencies = d["competencies"]
        if "interests" in d:
            user.interests = d["interests"]
        return user

    def to_dict(self) -> dict:
        return dict(
            email=self.email,
            competencies=self.competencies,
            interests=self.interests
        )


if __name__ == "__main__":
    o = User.from_dict({"id": "abc", "email": "a", "interests": ["a", "b", "c"]})
    print(o.to_dict())
    o = User.from_dict({"id": "abc", "email": "a", "password": "bottom"})
    print(o.to_dict())

    o = User.from_dict(
        {"id": "abc", "email": "a", "interests": ["a"], "competencies": ["A", "B"]})
    print(o.to_dict())
