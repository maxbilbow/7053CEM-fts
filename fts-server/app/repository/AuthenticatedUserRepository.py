from typing import Optional

from injector import singleton, inject
from app.database.Database import Database
import uuid

from app.model.AuthenticatedUser import AuthenticatedUser
from app.repository.AbstractRepository import AbstractRepository, TableConfig, Entity
from config import Config

TABLE = Config.get("database.table.users")


@singleton
class AuthenticatedUserRepository(AbstractRepository):
    @staticmethod
    def from_dict(d: dict) -> AuthenticatedUser:
        return AuthenticatedUser.from_dict(d)

    @staticmethod
    def to_dict(d: AuthenticatedUser) -> dict:
        return d.to_dict()

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

    def create_user(self, user: AuthenticatedUser):
        user.id = uuid.uuid4().hex
        return super().insert(user)

    def insert(self, entity: AuthenticatedUser) -> str:
        return self.create_user(entity)

    def find_user_by_email(self, email: str) -> Optional[AuthenticatedUser]:
        return self.find_one_by_props({"email": email})
