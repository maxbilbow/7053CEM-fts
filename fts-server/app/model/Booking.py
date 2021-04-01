from __future__ import annotations

from app.model.AbstractEntity import AbstractEntity


class Booking(AbstractEntity):
    training_event_id: str
    user_id: str

    def __init__(self, training_event_id: str, user_id: str):
        self.training_event_id = training_event_id
        self.user_id = user_id

    @staticmethod
    def from_dict(d: dict) -> Booking:
        return Booking(d["trainingEventId"], d["userId"])

    def to_dict(self: Booking) -> dict:
        return dict(
            id=self.id,
            trainingEventId=self.training_event_id,
            userId=self.user_id
        )


if __name__ == "__main__":
    s = Booking.from_dict({"trainingEventId": "a", "userId": "b"})
    print(s.to_dict())
