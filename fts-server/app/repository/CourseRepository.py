from injector import singleton, inject
from app.database.mongo import Database

from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.courses")


@singleton
class CourseRepository(AbstractRepository):

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

