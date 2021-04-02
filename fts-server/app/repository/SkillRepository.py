from injector import singleton, inject

from app.database.mongo import Database
from app.model.Skill import Skill
from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.skills")


@singleton
class SkillRepository(AbstractRepository[Skill]):

    @staticmethod
    def from_dict(d: dict) -> Skill:
        return Skill.from_dict(d)

    @staticmethod
    def to_dict(te: Skill) -> dict:
        return te.to_dict()

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

