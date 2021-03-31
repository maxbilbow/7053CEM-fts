from __future__ import annotations
from typing import Optional
from app.model.AbstractEntity import AbstractEntity


class AuthenticatedUser(AbstractEntity):
    id: str
    password: Optional[str, None]
    email: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(d: dict) -> AuthenticatedUser:
        user = AuthenticatedUser(email=d["email"], password=d["password"])
        if "id" in d:
            user.id = d["id"]
        return user

    def to_dict(self) -> dict:
        u_dict = dict(
            id=self.id,
            email=self.email
        )
        if self.password is not None:
            u_dict["password"] = self.password
        return u_dict


if __name__ == "__main__":
    o = AuthenticatedUser.from_dict({"id": "abc", "email": "a", "password": "bottom"})
    print(o.to_dict())
