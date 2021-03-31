from abc import abstractmethod
from typing import Generic, TypeVar, Optional, List, Generator

from app.database.Database import DbTable
from app.database.mongo import Database
from app.model.AbstractEntity import AbstractEntity


class TableConfig:
    def __init__(self, table_name: str):
        self.table_name = table_name


Entity = TypeVar('Entity', AbstractEntity, object)


class AbstractRepository(Generic[Entity]):
    _table: DbTable
    _database: Database
    _cfg = TableConfig

    def __init__(self, database: Database, table_config: TableConfig):
        self._database = database
        self._table = database.on(table_config.table_name)
        self._cfg = table_config

    @staticmethod
    @abstractmethod
    def from_dict(d: dict) -> Entity:
        raise NotImplementedError("from_dict")

    @staticmethod
    @abstractmethod
    def to_dict(d: Entity) -> dict:
        raise NotImplementedError("to_dict")

    def find_by_id(self, key: str) -> Optional[Entity]:
        d = self._table.find_by_id(key)
        return None if d is None else self.from_dict(d)

    def find_with_id_list(self, id_list: List[Entity]) -> List[Entity]:
        return self._table.find_many_by_id_list(id_list)

    def find_one_by_props(self, props: dict) -> Optional[Entity]:
        d = self._table.find_one_by_props(props)
        return self.from_dict(d) if d else None

    def find_many_by_props(self, props: dict) -> List[Entity]:
        return self._table.find_many_by_props(props)

    def insert(self, entity: Entity) -> str:
        return self._table.insert(self.to_dict(entity))

    def update(self, entity: Entity) -> object:
        return self._table.update(self.to_dict(entity))

    def find_one_by_id(self, entity_id: str) -> Optional[Entity]:
        d = self._table.find_by_id(entity_id)
        return None if d is None else self.from_dict(d)

    def find_all(self) -> Generator[Entity, None, None]:
        from_dict = self.from_dict

        def gen(results):
            for o in results:
                yield from_dict(o)

        return gen(self._table.find_all())

    def delete_by_id(self, entity_id: str) -> object:
        return self._table.delete_by_id(entity_id)


if __name__ == "__main__":
    pass
