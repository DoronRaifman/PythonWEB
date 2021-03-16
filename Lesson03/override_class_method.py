class Foo:
    def __init__(self, name, height):
        # instance members
        self.name = name
        self.height = height

    def __str__(self):
        return f'[{self.name}, {self.height}]'

    def __repr__(self):
        return str(self)


def new_str(myself):
    return(f'[{myself.name}, {myself.height}, {myself.phone}]')

if __name__ == '__main__':
    item1 = Foo('Doron', 180)
    print(f'item1: {item1}')
    item1.phone = '054-2150430'
    Foo.__str__ = lambda self: new_str(self)
    print(f'item1: {item1}')
