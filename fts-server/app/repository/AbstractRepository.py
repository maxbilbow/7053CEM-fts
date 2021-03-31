from app.database.Database import DbTable
from app.database.mongo import Database

class TableConfig:
    def __init__(self, table_name: str):
        self.table_name = table_name


class AbstractRepository:
    _table: DbTable
    _database: Database
    _cfg = TableConfig

    def __init__(self, database: Database, table_config: TableConfig):
        self._database = database
        self._table = database.on(table_config.table_name)
        self._cfg = table_config

    def find_by_id(self, key: str) -> dict:
        return self._table.find_by_id(key)

    def find_with_id_list(self, id_list: list) -> list:
        return self._table.find_many_by_id_list(id_list)

    def find_one_by_props(self, props: dict) -> dict:
        return self._table.find_one_by_props(props)

    def find_many_by_props(self, props: dict) -> list:
        return self._table.find_many_by_props(props)

    def insert(self, entity: dict) -> str:
        return self._table.insert(entity)

    def update(self, entity: dict) -> object:
        return self._table.update(entity)

    def find_one_by_id(self, entity_id: str) -> dict:
        return self._table.find_by_id(entity_id)

    def find_all(self):
        return self._table.find_all()

    def delete_by_id(self, entity_id: str) -> object:
        return self._table.delete_by_id(entity_id)
