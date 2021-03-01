class Foo:
    id = 1     # class member

    def __init__(self, name, height):
        # instance members
        self.name = name
        self.height = height
        self.id, Foo.id = Foo.id, Foo.id+1

    def __str__(self):
        return f'[{self.name}, {self.height}, id:{self.id}]'

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    item1 = Foo('Doron', 180)
    item2 = Foo('Adi', 163)
    print(f'item1: {item1}, item2: {item2}')
    item1.id = 6
    print(f'after override: {item1}, Foo.id:{Foo.id}')
    Foo.id = 7
    print(f'after Foo.id: {item1}, Foo.id:{Foo.id}')
    del item1.id
    print(f'after del: {item1}, Foo.id:{Foo.id}')
    item1.id = 10
    print(f'after item set: {item1}, Foo.id:{Foo.id}')
    item1.phone = '054-2150430'
    print(f'after add field: {item1}, phone:{item1.phone}')
    Foo.phone = '054-2150431'
    print(f'after add class field: {item2}, phone:{item2.phone}')


