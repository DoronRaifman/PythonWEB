from Lesson08.Core.DBInstance import DBInstance


class Worker:
    def __init__(self):
        self.table_items_name = 'items'
        self.table_users_name = 'users'

    def connect(self):
        DBInstance.connect()

    def disconnect(self):
        DBInstance.disconnect()

    def get_item_siblings(self, user_id: int, papa_id: int):
        records = DBInstance.find(
            self.table_items_name,
            where_clause=f"idusers={user_id} and papa_id={papa_id}",
            order_by="order_id ASC")
        return list(records)

    def find_item_by_id(self, user_id: int, item_id: int):
        records = DBInstance.find(
            self.table_items_name,
            where_clause=f"idusers={user_id} and iditems={item_id}")
        return records[0]

    def add_item(self, user_id: int, item_name: str,
                 papa_id: int = 0, order_id: int = 5):
        fields_data = {
            'idusers': user_id, 'item_name': item_name,
            'papa_id': papa_id, 'order_id': order_id}
        item_id = DBInstance.insert(self.table_items_name, fields_data)
        return item_id

    def update_item(self, user_id: int, item_id: int, item_fields: dict):
        res = DBInstance.update(self.table_items_name, item_fields,
                                where_clause=f"iditems={item_id}")
        return res

    def delete_items(self, user_id: int, item_id: int):
        DBInstance.delete(self.table_items_name, where_clause=f'iditems=item_id')

    def delete_item_with_all_siblings(self, user_id: int, item_id: int):
        pass
        # ToDo: implement method

    def delete_all_items(self):
        DBInstance.delete(self.table_items_name, where_clause='iditems > 0')

    def find_items_by_name(self, user_id: int, item_name: str):
        records = DBInstance.find(
            self.table_items_name,
            where_clause=f"idusers={user_id} and item_name='{item_name}'")
        return list(records)

    def find_items_by_name_start(self, user_id: int, item_name: str):
        records = DBInstance.find(
            self.table_items_name,
            where_clause=f"idusers={user_id} and item_name LIKE '{item_name}%'")
        return list(records)

    def find_user_by_name(self, user_name: str):
        records = DBInstance.find(
            self.table_users_name, where_clause=f"user_name='{user_name}'")
        return list(records)

    def find_user_by_id(self, user_id: int):
        records = DBInstance.find(
            self.table_users_name, where_clause=f"idusers={user_id}")
        return list(records)

    def fill_initial_data(self, user_id):
        table_name = 'items'
        list_names = ["חצי חינם", "טירה בשר", "סופר סופר", ]
        list_departments = [
            [("בכניסה", ["נייר טואלט", "אקונומיקה", "אבקת כביסה", ]),
             ("שתיה", ["7up", "מים", ]),
             ("מקרר", ["חלב", "גבינה צהובה", "קוטג", ]),
             ("בשר", ["כרעיים", "כנפיים", "שניצלים", ]),
             ],
            [("עמדה ראשית", ["אנטריקוט", "צלי כתף", ]),
             ("מקרר", ["שרימפס", "בשר טחון קפוא"]),
             ("המבורגרים", ["המבורגרים",]),
             ],
            [("שתיה", ["7up", "מים", ]),
             ("ירקות", ["עגבניות", "מלפפונים", ]),
             ("מוצרי חלב", ["חלב", "גבינה צהובה", "קוטג", ]),
             ],
        ]
        self.delete_all_items()
        for list_index in range(len(list_names)):
            papa_id = self.add_item(user_id, list_names[list_index], papa_id=0)
            departments = list_departments[list_index]
            for department_index in range(len(departments)):
                dep_name, items = departments[department_index]
                dep_id = self.add_item(user_id, dep_name, papa_id=papa_id)
                for item_name in items:
                    item_id = self.add_item(user_id, item_name, papa_id=dep_id)


if __name__ == '__main__':
    worker = Worker()
    worker.connect()
    worker.fill_initial_data(user_id=1)
    worker.disconnect()

