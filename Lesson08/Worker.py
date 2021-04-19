from Lesson08.Core.DBInstance import DBInstance


class Worker:
    def __init__(self):
        pass

    def connect(self):
        DBInstance.connect()

    def disconnect(self):
        DBInstance.disconnect()

    def get_item_siblings(self, papa_id):
        pass

    def item_list_to_dict_list(self, items_list):
        pass

    def find_item_by_id(self, item_id):
        pass

