# from flask import Flask, request, json, Response
from pymongo import MongoClient
from injector import singleton
import os
import uuid

from typing import Callable
from app.database.Database import Database

@singleton
class MongoDatabase(Database):
    def transaction(self, fn: Callable[[], None]):
        fn()

    def __init__(self):
        if (os.environ.get('FLASK_ENV') == 'development'):
            print("Connecting to local DEV database...")
            cluster = MongoClient('localhost', 27017)
        else:
            print("Connecting to remote production database...")
            cluster = MongoClient("mongodb+srv://" + str(os.environ.get(
                'SDP_COVID_DB_CREDENTIALS')) + "@cluster0.0bhm8.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")

        try:
            self.db = cluster["sdp_covid_dev"]
            self.db.command("ismaster")
        except Exception as e:
            print(e)
        else:
            print("You are connected!")

    def find_all_by_id(self, table_name: str, id_list: list) -> list:
        if not (table_name in self.db.collection_names()):
            return []
        table = self.db[table_name]
        result = []
        for poi in table.find({"id": {"$in": id_list}}):
            del poi["_id"]
            result.append(poi)
        return result

    def find_one_by_id(self, table_name: str, entity_id: str) -> dict:
        if not (table_name in self.db.collection_names()):
            return dict()
        table = self.db[table_name]
        result = table.find_one({"id": entity_id})
        if result:
            del result["_id"]
        return result

    def find_one_by_props(self, table_name: str, props: dict) -> dict:
        if not (table_name in self.db.collection_names()):
            return dict()
        table = self.db[table_name]
        result = table.find_one(props)
        if result:
            del result["_id"]
        return result

    def find_by_props(self, table_name: str, props: dict) -> list:
        if not (table_name in self.db.collection_names()):
            return []
        table = self.db[table_name]
        result = []
        for poi in table.find(props):
            del poi["_id"]
            result.append(poi)
        return result

    def update(self, table_name: str, entity: dict):
        if "id" in entity:
            entity["_id"] = entity["id"]

        table = self.db[table_name]
        newvalues = {"$set": entity}
        myquery = {"id": entity["id"]}
        return table.update_one(myquery, newvalues, upsert=True)

    def insert(self, table_name: str, entity: dict) -> str:
        if "id" in entity:
            entity["_id"] = entity["id"]
        else:
            entity["_id"] = entity["id"] = uuid.uuid4().hex

        table = self.db[table_name]
        return str(table.insert_one(entity).inserted_id)

    def delete_by_id(self, table_name: str, entity_id: str):
        table = self.db[table_name]
        return table.delete_one(table, {"id": entity_id})
