"""
We would like to configure video streamer (such as Kafka) to generate streaming configuration.
There is a simple (no loops) directional distribution requirements.
We need to generate (recursively), graph path from all graph roots (e.g. V0, V1).
We need to identify all pushers items and display only the ones that was already visited (e.g. T).
Pusher: some item which has a video frame and need to distribute this frame to more than 1 item.

Diagram:
V0 -> T -> Q -> D0
V0 -> T -> S -> D1
V1 -> S -> D1

Input example:
graph_data = [
{
    {'V0': ['T']},
    {'T': ['Q', 'S']},
    {'Q': ['D0']},
    {'S': ['D1']},
    {'V1': ['S']},
]

expected output:
result:
roots:
/V0/T/Q/D0
/V1/S/D1
pushers:
/T/S

Good luck.
"""


class GraphExercise:
    class Item:
        def __init__(self, item_id, item_list_keys):
            self.item_id = item_id
            self.item_list_keys = item_list_keys    # list of keys
            self.item_list = []                     # list of Item()
            self.papa_ids = []                      # papa id(s)
            self.is_visited = False

        def __str__(self):
            return f'Item:{self.item_id}, item_list_keys:{self.item_list_keys}, papa_ids:{self.papa_ids}, ' \
                   f'is_visited:{self.is_visited}'

        def __repr__(self):
            return str(self)

    def __init__(self, input_graph):
        self.input_graph = input_graph
        self.items = {}
        self.roots = []
        self.pushers = []

    def do_work(self):
        # create items
        for item_data in self.input_graph:
            item_id = list(item_data.keys())[0]
            item_list_keys = item_data[item_id]
            self.items[item_id] = item = self.Item(item_id, item_list_keys)
        # create missing items from item_list_keys and fill papa_ids
        for item_data in self.input_graph:
            papa_item_id = list(item_data.keys())[0]
            papa_item = self.items[papa_item_id]
            # create missing
            missing_leafs = [item_id for item_id in papa_item.item_list_keys if item_id not in self.items]
            for item_id in missing_leafs:
                self.items[item_id] = self.Item(item_id, [])
            # fill papa_ids
            for item_id in papa_item.item_list_keys:
                item = self.items[item_id]
                item.papa_ids.append(papa_item_id)
        # build item_list in items
        for item in self.items.values():
            item.item_list = [self.items[item_id] for item_id in item.item_list_keys]
        self.roots = [item for item in self.items.values() if len(item.papa_ids) == 0]
        self.pushers = [item for item in self.items.values() if len(item.item_list_keys) > 1]

    def print_items(self):
        print('items:')
        for item in self.items.values():
            print(f'\t{item}')
        print('roots:')
        print(f'\t{[item.item_id for item in self.roots]}')
        print('pushers:')
        print(f'\t{[item.item_id for item in self.pushers]}')

    def print_result(self):
        print('result:')
        print('roots:')
        for item in self.roots:
            self.print_recursive('', item)
        print('pushers:')
        for item in self.pushers:
            self.print_recursive_pushers('', item)

    def print_recursive(self, papa_path, item):
        if item.is_visited:
            return
        item.is_visited = True
        papa_path = f'{papa_path}/{item.item_id}'
        if len(item.item_list) == 0:
            print(f'{papa_path}')
        else:
            child_item = item.item_list[0]
            if child_item.is_visited:
                print(f'{papa_path}')
            else:
                self.print_recursive(papa_path, child_item)

    def print_recursive_pushers(self, papa_path, item):
        item.is_visited = False
        papa_path = f'{papa_path}/{item.item_id}'
        if len(item.item_list) > 1:
            for child_item in item.item_list[1:]:
                child_item.is_visited = False
                self.print_recursive(f'{papa_path}', child_item)


if __name__ == '__main__':
    # input_data = [
    #     {'V0': ['T']}, {'T': ['Q', 'S']}, {'Q': ['D0']}, {'S': ['D1']}, {'V1': ['S']},
    # ]
    input_data = [
        {'V0': ['T']}, {'T': ['Q', 'S', 'R']}, {'Q': ['D0']}, {'S': ['D1']}, {'V1': ['S']}, {'R': ['D2']},
    ]
    worker = GraphExercise(input_data)
    worker.do_work()
    worker.print_items()
    print('------------------')
    worker.print_result()
