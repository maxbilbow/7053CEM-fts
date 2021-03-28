from injector import singleton, inject
from app.database.mongo import Database
import uuid

TABLE = "user"

@singleton
class UserRepository:
    @inject
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user: dict):
        user["id"] = uuid.uuid4().hex
        return self.database.insert(TABLE, user)

    def find_user_by_email(self, email: str) -> dict:
        user = self.database.find_one_by_props(TABLE, {"email": email})
        return user
