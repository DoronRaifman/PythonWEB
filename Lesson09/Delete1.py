from Lesson09.Core.MongoInstance import MongoInstance, MongoDBException
import pymongo


class DeleteData1:
    def __init__(self):
        self.db_name = 'Lesson9'

    def do_work(self, query):
        collection_name = 'Family2'
        MongoInstance.connect(self.db_name, collection_name)
        result = MongoInstance.delete(query)
        print(result)
        MongoInstance.disconnect()


if __name__ == '__main__':
    worker = DeleteData1()
    query = {}
    # query = {'id': 300000005}
    worker.do_work(query)

