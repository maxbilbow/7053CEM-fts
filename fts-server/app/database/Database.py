from typing import Callable
from abc import abstractmethod

class Database:
    @abstractmethod
    def transaction(self, fn: Callable[[], None]):
        pass
