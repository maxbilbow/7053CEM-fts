from __future__ import annotations

from typing import List, Optional

from flask import jsonify

from app.model.AbstractEntity import AbstractEntity
from app.model.Competency import Competency
from app.model.User import User


class TrainingEvent(AbstractEntity):
    id: str
    training_manager_id: Optional[str]
    start_time: int
    title: str
    synopsis: str
    prerequisites: List[Competency]
    outcomes: List[Competency]
    attendees: Optional[List[User]]

    def __init__(self, title: str, id=None):
        self.id = id
        self.title = title
        self.synopsis = ""
        self.start_time = -1
        self.prerequisites = list()
        self.outcomes = list()
        self.attendees = list()

    @staticmethod
    def from_dict(d: dict) -> TrainingEvent:
        te = TrainingEvent(d["title"])
        if "id" in d:
            te.id = d["id"]
        if "synopsis" in d:
            te.synopsis = d["synopsis"]
        if "startTime" in d:
            te.start_time = d["startTime"]
        if "prerequisites" in d:
            pr = d["prerequisites"]
            te.prerequisites = list(map(lambda o: Competency.from_dict(o), pr))
        if "outcomes" in d:
            te.outcomes = list(map(lambda c: Competency.from_dict(c), d["outcomes"]))

        return te

    def to_json(self):
        u_dict = self.to_dict()
        del u_dict["password"]
        del u_dict["id"]
        return jsonify(u_dict)

    @staticmethod
    def to_dict(self) -> dict:
        u_dict = dict(
            id=self.id,
            title=self.title,
            synopsis=self.synopsis,
            startTime=self.start_time,
            prerequisites=list(map(lambda c: c.to_dict(c), self.prerequisites)),
            outcomes=list(map(lambda c: c.to_dict(c), self.outcomes))
        )
        return u_dict


if __name__ == "__main__":
    te = TrainingEvent.from_dict({
            "id": "title.lower()",
            "title": "TITLE",
            "outcomes": [{"skillId": "D", "level": 2}],
            "prerequisites": [{"skillId": "D", "level": 1}]
        })
    print(te.to_dict(te))
