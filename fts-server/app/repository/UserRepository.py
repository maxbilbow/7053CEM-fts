from typing import Optional

from injector import singleton, inject

from app.database.Database import Database
from app.model.User import User
from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.users")

@singleton
class UserRepository(AbstractRepository[User]):
    @staticmethod
    def from_dict(d: dict) -> User:
        return User.from_dict(d)

    @staticmethod
    def to_dict(u: User) -> dict:
        return u.to_dict()

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

    def find_user_by_email(self, email: str) -> Optional[User]:
        """
        Domain specific request
        :param email:
        :return: Matching user etity
        """
        return self.find_one_by_props({"email": email})
