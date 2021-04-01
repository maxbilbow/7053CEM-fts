import logging

from pymongo import MongoClient

from app.decorators.method import dev_only
from config import Config

DATABASE_NAME: str = Config.get("database.name")
CREDENTIALS: str = Config.get("database.mongodb.credentials")
PORT: int = Config.get("database.mongodb.port")


class MongoDb:
    _instance = None

    def __new__(cls, credentials=CREDENTIALS, port=PORT, database_name=DATABASE_NAME):
        if cls._instance is None:
            print('Creating the database')
            cls._instance = super(MongoDb, cls).__new__(cls)
            cls._database_name = database_name
            print("Connecting to database...")
            cls._cluster = MongoClient('mongodb://{}'.format(credentials), port)
            cls._db = cls._instance._cluster[database_name]
        return cls._instance

    @staticmethod
    def table(table_name: str):
        return MongoDb()._db[table_name]

    @staticmethod
    def collection_names():
        return MongoDb()._db.collection_names()

    @staticmethod
    @dev_only
    def drop(collection: str):
        logging.warning("Dropping collection: {}".format(collection))
        MongoDb()._db.drop_collection(collection)

    @staticmethod
    @dev_only
    def set_credentials(credentials: str, port: int):
        MongoDb._instance = None
        MongoDb(credentials, port)


if __name__ == "__main__":
    credentials = "localhost"
    table = MongoDb.table("test")
    print(table.insert_one({"test": "bob"}).inserted_id)
    table = MongoDb.table("test")
