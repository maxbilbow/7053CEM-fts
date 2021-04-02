from injector import singleton, inject

from app.database.mongo import Database
from app.model.TrainingEvent import TrainingEvent
from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.training_events")

@singleton
class TrainingEventRepository(AbstractRepository[TrainingEvent]):

    @staticmethod
    def from_dict(d: dict) -> TrainingEvent:
        return TrainingEvent.from_dict(d)

    @staticmethod
    def to_dict(te: TrainingEvent) -> dict:
        return te.to_dict()

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))
