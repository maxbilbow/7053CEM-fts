from __future__ import annotations

from typing import List, Optional

from flask import jsonify

from app.model.AbstractEntity import AbstractEntity


class TrainingEvent(AbstractEntity):
    training_manager_id: Optional[str]
    start_time: int
    title: str
    synopsis: str
    prerequisites: List[str]
    outcomes: List[str]

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
            te.prerequisites = d["prerequisites"]
        if "outcomes" in d:
            te.outcomes = d["outcomes"]

        return te

    def to_dict(self) -> dict:
        u_dict = dict(
            id=self.id,
            title=self.title,
            synopsis=self.synopsis,
            startTime=self.start_time,
            prerequisites=self.prerequisites,
            outcomes=self.outcomes
        )
        return u_dict


if __name__ == "__main__":
    te = TrainingEvent.from_dict({
            "id": "title.lower()",
            "title": "TITLE",
            "outcomes": ["A", "B"],
            "prerequisites": ["C", "D"]
        })
    print(te.to_dict())
