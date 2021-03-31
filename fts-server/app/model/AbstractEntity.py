from __future__ import annotations
from abc import abstractmethod


class AbstractEntity:

    @staticmethod
    @abstractmethod
    def from_dict(d: dict) -> AbstractEntity:
        pass

    @staticmethod
    @abstractmethod
    def to_dict(e: AbstractEntity) -> dict:
        pass

