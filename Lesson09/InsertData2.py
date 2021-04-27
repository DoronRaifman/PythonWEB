from Lesson09.Core.MongoInstance import MongoInstance, MongoDBException


class InsertData:
    def __init__(self):
        self.db_name = 'Lesson9'

    def do_work_relational(self):
        collection_name = 'Family2'
        MongoInstance.connect(self.db_name, collection_name)
        data_relational = [
            {'name': 'Doron', 'id': 100000000, 'phone': '054-2150430',
             'siblings': [30000001, 30000002, 30000003]},
            {'name': 'Tomer', 'id': 30000001, 'siblings': [300000004]},
            {'name': 'Gal', 'id': 30000002},
            {'name': 'Raz', 'id': 30000003},
            {'name': 'Yarden', 'id': 300000004},
        ]
        MongoInstance.insert_many(data_relational)
        MongoInstance.disconnect()


if __name__ == '__main__':
    worker = InsertData()
    worker.do_work_relational()

