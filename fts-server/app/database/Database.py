from __future__ import annotations
from typing import Callable, Optional, List
from abc import abstractmethod


class Database:
    def on(self, table_name: str) -> DbTable:
        return DbTable(table_name, self)

    @abstractmethod
    def transaction(self, fn: Callable[[], None]):
        pass

    @abstractmethod
    def find_by_id(self, table_name: str, key: str) -> Optional[dict]:
        pass

    @abstractmethod
    def find_one_by_props(self, table_name: str, props: dict) -> Optional[dict]:
        pass

    @abstractmethod
    def find_many_by_props(self, table_name: str, props: dict) -> list:
        pass

    @abstractmethod
    def insert(self, table_name: str, entity: dict) -> str:
        pass

    @abstractmethod
    def update(self, table_name: str, entity: dict) -> object:
        pass

    @abstractmethod
    def find_many_by_id_list(self, table_name: str, id_list: list) -> list:
        pass

    @abstractmethod
    def find_all(self, table_name: str) -> list:
        pass

    @abstractmethod
    def delete_by_id(self, table_name: str, entity_id: str) -> object:
        pass


class DbTable:
    __table_name: str
    __db: Database

    def __init__(self, table_name, database: Database):
        self.__table_name = table_name
        self.__db = database

    def find_by_id(self, key: str) -> Optional[dict]:
        return self.__db.find_by_id(self.__table_name, key)

    def find_one_by_props(self, props: dict) -> Optional[dict]:
        return self.__db.find_one_by_props(self.__table_name, props)

    def find_many_by_props(self, props: dict) -> list:
        return self.__db.find_many_by_props(self.__table_name, props)

    def insert(self, entity: dict) -> str:
        return self.__db.insert(self.__table_name, entity)

    def update(self, entity: dict) -> object:
        return self.__db.update(self.__table_name, entity)

    def find_many_by_id_list(self, id_list: list) -> list:
        return self.__db.find_many_by_id_list(self.__table_name, id_list)

    def find_all(self):
        return self.__db.find_all(self.__table_name)

    def delete_by_id(self, entity_id: str) -> object:
        return self.__db.delete_by_id(self.__table_name, entity_id)


