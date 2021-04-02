from typing import Iterable, Optional, Callable

from mock_app.database.Database import Database


class MockDb(Database):
    def transaction(self, fn: Callable[[], None]):
        pass

    def find_one_by_props(self, table_name: str, props: dict) -> Optional[dict]:
        pass

    def find_many_by_props(self, table_name: str, props: dict) -> Iterable[dict]:
        pass

    def insert(self, table_name: str, entity: dict) -> str:
        pass

    def update(self, table_name: str, entity: dict) -> object:
        pass

    def find_many_by_id_list(self, table_name: str, id_list: list) -> Iterable[dict]:
        pass

    def find_all(self, table_name: str) -> Iterable[dict]:
        pass

    def delete_by_id(self, table_name: str, entity_id: str) -> object:
        pass