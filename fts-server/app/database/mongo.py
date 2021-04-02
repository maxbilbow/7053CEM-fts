# from flask import Flask, request, json, Response
import json

from flask import jsonify
from injector import singleton
import uuid

from typing import Callable, Iterable, Optional

from app.database.MongoDB import MongoDb
from app.database.Database import Database
import logging


@singleton
class MongoDatabase(Database):

    def transaction(self, fn: Callable[[], None]):
        fn()

    def find_many_by_id_list(self, table_name: str, id_list: list) -> list:
        if not (table_name in MongoDb.collection_names()):
            return []
        table = MongoDb.table(table_name)
        return list(table.find({"id": {"$in": id_list}}, projection={"_id": 0}))

    def find_one_by_props(self, table_name: str, props: dict) -> Optional[dict]:
        if not (table_name in MongoDb.collection_names()):
            return None
        table = MongoDb.table(table_name)
        return table.find_one(props, {"_id": 0})

    def find_many_by_props(self, table_name: str, props: dict) -> list:
        if not (table_name in MongoDb.collection_names()):
            return []
        table = MongoDb.table(table_name)
        return list(table.find(props, projection={"_id": 0}))

    def update(self, table_name: str, entity: dict):
        if "id" in entity:
            entity["_id"] = entity["id"]

        table = MongoDb.table(table_name)
        newvalues = {"$set": entity}
        myquery = {"id": entity["id"]}
        return table.update_one(myquery, newvalues, upsert=True)

    def insert(self, table_name: str, entity: dict) -> str:
        if "id" in entity:
            entity["_id"] = entity["id"]

        table = MongoDb.table(table_name)
        logging.info("into table: {}", table)
        return str(table.insert_one(entity).inserted_id)

    def delete_by_id(self, table_name: str, entity_id: str):
        table = MongoDb.table(table_name)
        return table.delete_one(table, {"id": entity_id})

    def find_all(self, table_name: str) -> Iterable:
        table = MongoDb.table(table_name)
        return table.find(projection={"_id": 0})
