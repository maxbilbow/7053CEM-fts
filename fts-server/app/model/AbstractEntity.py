from __future__ import annotations
from abc import abstractmethod


class AbstractEntity:
    id: str

    @staticmethod
    @abstractmethod
    def from_dict(d: dict) -> AbstractEntity:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
