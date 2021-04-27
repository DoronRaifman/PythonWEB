from Lesson09.Core.MongoInstance import MongoInstance, MongoDBException


class InsertData:
    def __init__(self):
        self.db_name = 'Lesson9'

    def do_work_hierarchical(self):
        collection_name = 'Family1'
        MongoInstance.connect(self.db_name, collection_name)
        data_hierarchical = {
            'name': 'Doron', 'id': 55445837, 'phone': '054-2150430',
            'height': 180,
            'siblings': [
                {'name': 'Tomer', 'phone': '054 - 1234567',
                 'siblings': [{'name': 'Yarden'}]},
                {'name': 'Gal', 'phone': '054-1234567'},
                {'name': 'Raz', 'phone': '054 - 1234567'},
            ]
        }
        MongoInstance.insert(data_hierarchical)
        MongoInstance.disconnect()


if __name__ == '__main__':
    worker = InsertData()
    worker.do_work_hierarchical()

