class BaseDict:
    def __init__(self, items_count):
        self.items_count = items_count
        self.dict_data = {}

    def add(self, value):
        raise Exception('Bad call')

    def find(self, value):
        raise Exception('Bad call')

    def fill(self):
        for i in range(self.items_count):
            self.add(i)

    def find_all(self):
        for i in range(self.items_count):
            self.find(i)


class NormalDict(BaseDict):
    def __init__(self, items_count):
        super().__init__(items_count)

    def add(self, value):
        item_data = f'key {value}, val {value}'
        self.dict_data[value] = item_data

    def find(self, value):
        return self.dict_data[value]


class SuperbDict(BaseDict):
    def __init__(self, items_count, hash_divider):
        super().__init__(items_count)
        self.hash_divider = hash_divider

    def add(self, value):
        hash_code = int(value // self.hash_divider)
        item_data = f'key {hash_code}, val {value}'
        if hash_code not in self.dict_data:
            self.dict_data[hash_code] = {value: item_data}
        else:
            self.dict_data[hash_code][value] = item_data

    def find(self, value):
        return self.dict_data[int(value // self.hash_divider)][value]


if __name__ == '__main__':
    items_count, hash_divider = 1000000, 1000
    # convert code to data
    superb, normal = \
        SuperbDict(items_count, hash_divider), NormalDict(items_count)
    todo_list = [
        {'name': 'superb', 'object': superb,
         'steps': (('fill', superb.fill), ('find', superb.find_all))},
        {'name': 'normal', 'object': normal,
         'steps': (('fill', normal.fill), ('find', normal.find_all))},
    ]
    import time
    for task in todo_list:
        task_name, task_obj = task['name'], task['object']
        line = f'{task_name}: '
        for step in task['steps']:
            step_name, step_func = step     # unpack tuple
            start_time = time.time()
            step_func()
            elapsed = time.time() - start_time
            line += f'{step_name} {elapsed:.3f}, '
        print(line[:-2])    # remove ', ' from the end of line

