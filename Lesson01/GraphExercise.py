
class GraphExercise:
    class Item:
        def __init__(self, item_id, item_list_keys):
            self.item_id = item_id
            self.item_list_keys = item_list_keys    # list of keys
            self.item_list = []                     # list of Item()
            self.pointed_by = []                    # pointed by keys
            self.is_visited = False
            self.is_pusher = False

    def __init__(self, input_graph):
        self.input_graph = input_graph
        self.items = {}
        self.roots = []
        self.pushers = []

    def do_work(self):
        # create items
        self.items = {list(item_dict.keys)[0]: self.Item(item_id, item_list_keys)
                      for item_dict in self.input_graph}
        # create item list for all items
        for item_id, item in self.items.items():
            item.item_list = [self.items[item_id] for item_id in item.item_list_keys]
            item.pointed_by = item.item_list
        self.roots = [item for item in self.items.values() if len(item.pointed_by) == 0]
        self.pushers = [item for item in self.items.values() if len(item.item_list) > 1]
        print('')

if __name__ == '__main__':
    input_data = [
        {'V0': ['T']}, {'T': ['Q', 'S']}, {'Q': ['D0']}, {'S': ['D1']}, {'V1': ['S']},
    ]
    worker = GraphExercise(input_data)
    worker.do_work()
