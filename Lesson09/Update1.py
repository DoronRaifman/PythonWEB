from Lesson09.Core.MongoInstance import MongoInstance, MongoDBException
import pymongo


class UpdateData1:
    def __init__(self):
        self.db_name = 'Lesson9'

    def do_work(self):
        collection_name = 'Family2'
        MongoInstance.connect(self.db_name, collection_name)
        gal_id = 30000002
        query = {'id': gal_id}
        records = MongoInstance.find(query)
        gal_record = records[0]
        del gal_record['_id']
        print(f'Gal1: {gal_record}')
        gal_siblings = gal_record['siblings'] if 'siblings' in gal_record else []

        new_child_id = 300000005
        new_child = {'name': 'New Child', 'id': new_child_id}
        MongoInstance.insert(new_child)

        gal_siblings.append(new_child_id)
        gal_record['siblings'] = gal_siblings
        MongoInstance.update(query, gal_record)
        print(f'Gal2: {gal_record}')

        MongoInstance.disconnect()


if __name__ == '__main__':
    worker = UpdateData1()
    worker.do_work()

