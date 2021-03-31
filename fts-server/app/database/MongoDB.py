from pymongo import MongoClient
from config import Config

database_name: str = Config.get("database.name")
data_in_table_name: str = Config.get("database.table.users")
credentials = Config.get("database.mongodb.credentials")
port = Config.get("database.mongodb.port")


class MongoDb:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the database')
            cls._instance = super(MongoDb, cls).__new__(cls)
            cls._database_name = database_name
            print("Connecting to database...")
            cls._cluster = MongoClient('mongodb://{}'.format(credentials), port)
            cls._db = cls._cluster[database_name]
        return cls._instance

    @staticmethod
    def table(table_name: str):
        return MongoDb()._db[table_name]

    @staticmethod
    def collection_names():
        return MongoDb()._db.collection_names()


if __name__ == "__main__":
    credentials = "localhost"
    table = MongoDb.table("test")
    print(table.insert_one({"test": "bob"}).inserted_id)
    table = MongoDb.table("test")
