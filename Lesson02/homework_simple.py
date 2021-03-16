class NormalDict:
    def __init__(self, items_count):
        self.items_count = items_count
        self.dict_data = {}

    def add(self, value):
        item_data = f'key {value}, val {value}'
        self.dict_data[value] = item_data

    def find(self, value):
        return self.dict_data[value]

    def fill(self):
        for i in range(self.items_count):
            self.add(i)

    def find_all(self):
        for i in range(self.items_count):
            self.find(i)


class SuperbDict:
    def __init__(self, items_count, hash_divider):
        self.items_count = items_count
        self.hash_divider = hash_divider
        self.dict_data = {}

    def add(self, value):
        hash_code = int(value // self.hash_divider)
        item_data = f'key {hash_code}, val {value}'
        if hash_code not in self.dict_data:
            self.dict_data[hash_code] = {value: item_data}
        else:
            self.dict_data[hash_code][value] = item_data

    def find(self, value):
        return self.dict_data[int(value // self.hash_divider)][value]

    def fill(self):
        for i in range(self.items_count):
            self.add(i)

    def find_all(self):
        for i in range(self.items_count):
            self.find(i)


if __name__ == '__main__':
    items_count, hash_divider = 1000000, 1000
    # convert code to data
    superb, normal = SuperbDict(items_count, hash_divider), NormalDict(items_count)

    import time
    start_time = time.time()
    superb.fill()
    step_time, elapsed_fill = time.time(), time.time() - start_time
    superb.find_all()
    elapsed_find = time.time() - step_time
    print(f'superb: fill {elapsed_fill:.3f}, find {elapsed_find:.3f}')

    start_time = time.time()
    normal.fill()
    step_time, elapsed_fill = time.time(), time.time() - start_time
    normal.find_all()
    elapsed_find = time.time() - step_time
    print(f'normal: fill {elapsed_fill:.3f}, find {elapsed_find:.3f}')
