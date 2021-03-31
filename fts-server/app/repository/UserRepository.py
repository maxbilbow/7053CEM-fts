from injector import singleton, inject
from app.database.Database import Database
import uuid

from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.users")

@singleton
class UserRepository(AbstractRepository):
    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

    def create_user(self, user: dict):
        user["id"] = uuid.uuid4().hex
        return self.insert(user)

    def find_user_by_email(self, email: str) -> dict:
        return self.find_one_by_props({"email": email})
