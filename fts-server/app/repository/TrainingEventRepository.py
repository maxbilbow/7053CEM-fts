from injector import singleton, inject
from app.database.mongo import Database
from app.model.TrainingEvent import TrainingEvent

from app.repository.AbstractRepository import AbstractRepository, TableConfig, Entity
from config import Config

TABLE = Config.get("database.table.courses")


@singleton
class TrainingEventRepository(AbstractRepository):

    @staticmethod
    def from_dict(d: dict) -> TrainingEvent:
        return TrainingEvent.from_dict(d)

    @staticmethod
    def to_dict(te: TrainingEvent) -> dict:
        return TrainingEvent.to_dict(te)

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

