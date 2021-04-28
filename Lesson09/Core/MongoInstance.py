# Mongo instance
import pymongo
from pymongo import MongoClient


class MongoDBException(Exception):
    pass


class MongoInstance:
    connect_str = "mongodb://localhost:27017"
    client = MongoClient(connect_str)
    db = None
    db_collection: pymongo.collection = None

    @classmethod
    def connect(cls, db_name: str, collection_name: str):
        try:
            cls.db = cls.client[db_name]
            cls.db_collection = cls.db[collection_name]
        except Exception as ex:
            cls.generate_exception("connect", ex)

    @classmethod
    def disconnect(cls):
        try:
            cls.client.close()
        except Exception as ex:
            cls.generate_exception("disconnect", ex)

    @classmethod
    def replace_collection(cls, new_collection):
        cls.db_collection = cls.db[new_collection]

    @classmethod
    def is_connected(cls):
        return cls.client is not None and cls.db is not None and cls.db_collection is not None

    @classmethod
    def insert(cls, data: dict):
        try:
            res = cls.db_collection.insert_one(data)
        except Exception as ex:
            res = None
            cls.generate_exception("insert", ex)
        return res

    @classmethod
    def insert_many(cls, data_list: list):
        try:
            res = cls.db_collection.insert_many(data_list)
        except Exception as ex:
            res = None
            cls.generate_exception("insert_many", ex)
        return res

    @classmethod
    def update(cls, query: dict, data: dict):
        try:
            res = cls.db_collection.update_one(
                query, {"$set": data}, upsert=True)
        except Exception as ex:
            res = None
            cls.generate_exception("update", ex)
        return res

    @classmethod
    def find(cls, query: dict, sort_cmd=None):
        try:
            find_result = cls.db_collection.find(filter=query)
            if sort_cmd is not None:
                find_result = find_result.sort(sort_cmd)
        except Exception as ex:
            find_result = None
            cls.generate_exception("find", ex)
        result = [record for record in find_result]
        return result

    @classmethod
    def find_limit(cls, query: dict, sort_id: str, days_back_count: int):
        try:
            find_result = cls.db_collection.find(
                filter=query).limit(days_back_count).sort(
                [(sort_id, pymongo.DESCENDING)])
        except Exception as ex:
            find_result = None
            cls.generate_exception("find_limit", ex)
        result = [record for record in find_result]
        return result

    @classmethod
    def delete(cls, query: dict):
        try:
            res = cls.db_collection.delete_many(filter=query)
            res1 = res.deleted_count
        except Exception as ex:
            res1 = None
            cls.generate_exception("delete", ex)
        return f"{res1}, documents deleted."

    @classmethod
    def delete_all(cls):
        return cls.delete({})

    @classmethod
    def find_and_update(cls, query:dict, update:dict):
        """
        find_and_update
        :param query
        :param update
        :return: updated record
        update example:
            {'$set': {'name': 'doron', }, '$inc': {'counter': 1, }}
        """
        record = cls.db_collection.find_one_and_update(
            filter=query, update=update, upsert=True, new=True)
        return record

    @classmethod
    def update_and_fetch_in_transaction(cls, data: dict, find_query: dict, update_query: dict, update_cmd=None):
        result = []
        try:
            update_statement = {"$set": data}
            if update_cmd is not None:
                for key, val in update_cmd.items():
                    update_statement[key] = val
            insert_result = cls.find_and_update(update_query, update_statement)
            find_result = cls.db_collection.find(filter=find_query)
            result = [record for record in find_result]
            if insert_result not in result:
                result.append(insert_result)
        except Exception as ex:
            result = []
            cls.generate_exception("insert_and_fetch_in_transaction", ex)
        return result

    @classmethod
    def find_first_id_and_delete(cls):
        # Note that if server is stopped in pycharm the message will be deleted and will not be calculated!
        # it is small penalty with significant performance gain
        try:
            record = cls.db_collection.find_one_and_delete(filter={}, sort=[('_id', pymongo.ASCENDING)])
            # note: Mongo is implemented using lazy access strategy
        except Exception as ex:
            line = f"@@@ MongoDB Exception in find_first_id_and_delete, exception: {str(ex)}"
            print(line)
            raise MongoDBException(line)
        return record

    @classmethod
    def create_index(cls, key):
        cls.db_collection.create_index()

    @classmethod
    def count_documents(cls):
        count = cls.db_collection.count_documents(filter={})
        return count

    @staticmethod
    def generate_exception(info: str, exception):
        line = f"@@@ MongoDB Exception in {info}," \
               f" exception: {str(exception)}"
        print(line)
        raise MongoDBException(line)


