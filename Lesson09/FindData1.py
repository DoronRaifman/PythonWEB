import pymongo
from Lesson09.Core.MongoInstance import MongoInstance, MongoDBException


class FindData:
    def __init__(self):
        self.db_name = 'Lesson9'

    def do_work(self):
        collection_name = 'Family2'
        MongoInstance.connect(self.db_name, collection_name)
        query1 = {'id': 100000000}
        records = MongoInstance.find(query1)
        doron_record = records[0]
        del doron_record['_id']
        print(f'Doron: {doron_record}')

        direct_siblings = doron_record['siblings']  # list
        query2 = {'id': {'$in': direct_siblings}}
        sort_cmd = [('name', pymongo.ASCENDING)]
        records = MongoInstance.find(query2, sort_cmd)
        for i, record in enumerate(records):
            del record['_id']
            print(f'{i}: {record}')
        MongoInstance.disconnect()


if __name__ == '__main__':
    worker = FindData()
    worker.do_work()

